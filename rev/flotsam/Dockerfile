FROM rust:1-slim-buster as builder

WORKDIR /app
COPY flotsam_wasm/ ./flotsam_wasm

WORKDIR /app/flotsam_wasm
RUN cargo update
RUN cargo install wasm-pack
RUN wasm-pack build

FROM node:20-buster-slim as frontend

WORKDIR /app

RUN mkdir /app/flotsam_frontend
RUN mkdir /app/flotsam_wasm

# frontend node project
COPY flotsam_frontend/package.json /app/flotsam_frontend
COPY flotsam_frontend/package-lock.json /app/flotsam_frontend

# Copy the rest of the files over
WORKDIR /app/flotsam_frontend
COPY flotsam_frontend/config/ ./config/
COPY flotsam_frontend/public/ ./public/
COPY flotsam_frontend/src/ ./src/

RUN npm install

WORKDIR /app/flotsam_wasm
COPY --from=builder /app/flotsam_wasm/pkg/ ./pkg/

WORKDIR /app/flotsam_frontend
RUN npm run build

# serve
RUN npm install -g serve
CMD ["serve", "-s", "build"]