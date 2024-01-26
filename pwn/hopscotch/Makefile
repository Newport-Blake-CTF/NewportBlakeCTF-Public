GCC=docker run --platform=linux/arm64 --rm -w /build -v $(CURDIR):/build -it gcc
DEV=docker run --platform linux/arm64/v8 --rm -w /tmp/pwn -v $(CURDIR):/tmp/pwn -e QEMU_GDB=1337 -p 1337:1337 -it ubuntu:22.04
RUN=docker run --platform linux/arm64/v8 --rm -w /tmp/pwn -v $(CURDIR):/tmp/pwn -it ubuntu:22.04
CHAL=hopscotch

.PHONY: all build

all: build

build:
	$(GCC) gcc hopscotch.c -o runner -mbranch-protection=none -fno-stack-protector -Wl,-z,norelro -Wl,-z,lazy -pie -fPIC

dev: build
	$(DEV) ./runner

run: build
	$(RUN) ./runner

dump: build
	$(GCC) objdump -d runner

package:
	-rm dist.tar
	cd .. && tar -czf $(CHAL)/dist.tar \
		$(CHAL)/Dockerfile \
		$(CHAL)/runner \
		$(CHAL)/qemu-aarch64 \
		$(CHAL)/run.sh \
		$(CHAL)/lib