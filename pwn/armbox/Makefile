RUN=docker run --rm --platform linux/amd64 -w /pwn -v $(CURDIR):/pwn -it armbox
CROSS=docker run --rm --platform linux/arm/v7 -w /pwn -v $(CURDIR):/pwn -it gcc
CHAL=armbox

.PHONY: all armbox filter build run

all: build

armbox:
	docker build . -f armbox.dockerfile -t armbox

filter:
	gcc $(pkg-config --cflags --libs glib-2.0) -fPIC -shared filter.c -o libfilter.so

build:
	$(CROSS) gcc armbox.c -o armbox -Wl,-rpath,.

run:
	$(RUN) qemu-arm -plugin ./libfilter.so ./armbox

solve:
	$(CROSS) as solve.s -o solve.o
	$(CROSS) ld solve.o -o solve.elf
	$(CROSS) objcopy -O binary solve.elf solve.bin

package:
	-rm dist.tar
	cd .. && tar -czf $(CHAL)/dist.tar \
		$(CHAL)/Dockerfile \
		$(CHAL)/$(CHAL) \
		$(CHAL)/libfilter.so \
		$(CHAL)/run.sh \
		$(CHAL)/lib