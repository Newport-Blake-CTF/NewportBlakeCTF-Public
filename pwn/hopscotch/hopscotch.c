#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>
#include <fcntl.h>
#include <stdint.h>

#define BUFSZ 0x4000

int bad_pwner_returning_to_main = 0;

__attribute__((section(".plt"), leaf))
void filler() {
    asm volatile(
        ".rept  0x10000 / 4\n"
        "nop\n"
        ".endr\n"
        "udf #0\n"
    );
}

int main(int argc, char **argv) {
    char *address, *old, *new;
    int fd;
    int status;
    char buf[BUFSZ];

    if (bad_pwner_returning_to_main > 0) {
        asm volatile("udf #0");
    }
    bad_pwner_returning_to_main++;

    setbuf(stdout, NULL);
    setbuf(stdin, NULL);

    fd = open("/proc/self/maps", O_RDONLY);
    read(fd, buf, BUFSZ);

    old = buf;
    while ((new = strchr(old, '\n'))) {
        *new = 0;
        if (strstr(old, "run")) {
            puts(old);
        }
        old = new + 1;
    }

    puts("exit status >");
    read(0, buf, BUFSZ);
    status = strtol(buf, NULL, 16);

    puts("address >");
    read(0, buf, BUFSZ);
    address = (char *)strtol(buf, NULL, 16);

    puts("character >");
    read(0, buf, BUFSZ);
    *address = buf[0];
    
    printf("exiting with status: %d\n", status);
    exit(status);
}