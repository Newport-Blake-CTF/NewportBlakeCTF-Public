FROM debian:bullseye-slim AS build

RUN apt-get update && apt-get install -y gcc

COPY ./sands.c /app/sands.c
RUN gcc -static -o /app/run /app/sands.c

FROM pwn.red/jail

COPY --from=build / /srv
COPY ./flag.txt /srv/app/flag.txt

RUN chmod 755 /srv/app/run

ENV JAIL_TIME=30