GCC=docker run --platform=linux/arm/v7 --rm -w /build -v $(CURDIR):/build -it gcc
CHAL=wheres-my-win-function

.PHONY: all build

all: build

build:
	$(GCC) gcc wheres-my-win-function.c -o wmwf -fno-stack-protector -no-pie -Wl,-z,lazy -O1

package:
	-rm dist.tar
	cd .. && tar -czf $(CHAL)/dist.tar \
		$(CHAL)/Dockerfile \
		$(CHAL)/wheres-my-win-function.c \
		$(CHAL)/wmwf \
		$(CHAL)/qemu-arm \
		$(CHAL)/run.sh \
		$(CHAL)/lib