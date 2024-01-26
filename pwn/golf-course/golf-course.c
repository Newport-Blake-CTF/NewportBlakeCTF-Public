#define  _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <fcntl.h>
#include <unistd.h>

int main() {
    char elf[64];
    char cmd[128];

    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
    
    int fd = memfd_create("golf-course", 0);

    printf("elf file: ");
    ftruncate(fd, 64);
    read(0, elf, 64);
    write(fd, elf, 64);

    sprintf(cmd, "qemu-aarch64-static /proc/%d/fd/%d", getpid(), fd);
    system(cmd);
}