FROM --platform=linux/arm/v7 ubuntu:22.04 as cross

FROM --platform=linux/amd64 ubuntu:22.04

RUN apt-get update && \
    apt-get install -y \
        qemu-user gcc
COPY --from=cross /lib/ld-linux-armhf.so.3 /lib/ld-linux.so.3
COPY --from=cross /lib/arm-linux-gnueabihf/libc.so.6 /lib/arm-linux-gnueabihf/libc.so.6