RUN=docker run --platform linux/arm/v5 -w /app -v "$(CURDIR)":/app -t gcc:latest
CHAL=ret2thumb

all: build

build: $(CHAL).c
	$(RUN) gcc $(CHAL).c -o $(CHAL) -no-pie -fno-stack-protector -Wl,-z,now -marm
	$(RUN) strip -w -N '$$*' $(CHAL)

dump: build
	$(RUN) objdump -d $(CHAL)

package:
	-rm dist.tar
	cd .. && tar -czf $(CHAL)/dist.tar \
		$(CHAL)/Dockerfile \
		$(CHAL)/ret2thumb \
		$(CHAL)/qemu-arm \
		$(CHAL)/run.sh \
		$(CHAL)/lib