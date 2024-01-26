FROM --platform=linux/arm/v7 ubuntu:22.04

RUN apt-get update && \
    apt-get install -y \
    gcc