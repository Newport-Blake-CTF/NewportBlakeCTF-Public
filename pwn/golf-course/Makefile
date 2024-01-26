RUN=docker run --rm --platform=linux/arm64 -w /pwn -v $(CURDIR):/pwn -t gcc
DEP=docker run --rm --platform=linux/amd64 -w /pwn -v $(CURDIR):/pwn -t gcc
NAME=bflt

all: build

build:
	$(RUN) as $(NAME).s -o $(NAME).o # -mbig-endian
	$(RUN) objcopy -O binary $(NAME).o $(NAME)

dump:
	$(RUN) objdump -D -b binary -m armv8-a $(NAME)

chal:
	$(DEP) gcc golf-course.c -o golf-course