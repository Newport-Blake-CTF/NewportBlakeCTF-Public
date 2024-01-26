FROM --platform=linux/amd64 ubuntu:23.04 as build

WORKDIR /blockchain

RUN apt-get update && \
    apt-get install -y \
    gcc cargo bzip2 git

RUN git clone --depth 1 --branch v0.8.0 https://github.com/solana-labs/rbpf
COPY chal/Cargo.toml .
COPY chal/src src

COPY chal/rbpf.diff .
RUN cd rbpf && git apply ../rbpf.diff

RUN cargo build --release

COPY chal/blockchain.c .
RUN gcc blockchain.c -lblockchain -Ltarget/release -o blockchain -Wl,-rpath,.