CROSS=docker run --rm --platform linux/arm/v7 -w /pwn -v $(CURDIR):/pwn -it mine
CHAL=canary-in-a-coal-mine

.PHONY: all build run mine

all: build

mine:
	docker build . -f build.dockerfile -t mine

build: mine
	$(CROSS) gcc coal-mine.c -o coal-mine -fstack-protector-strong -no-pie

dump:
	$(CROSS) objdump -d coal-mine

package:
	-rm dist.tar
	cd .. && tar -czf $(CHAL)/dist.tar \
		$(CHAL)/Dockerfile \
		$(CHAL)/coal-mine.c \
		$(CHAL)/coal-mine \
		$(CHAL)/run.sh \
		$(CHAL)/lib