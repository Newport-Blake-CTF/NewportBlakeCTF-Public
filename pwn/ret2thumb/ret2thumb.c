#include <stdio.h>

void vuln() {
    char buf[32];

    puts("Can you ret2thumb? ");
    gets(buf);
    return;
}

int main() {
    setvbuf(stdin, 0, _IONBF, 0);
    setvbuf(stdout, 0, _IONBF, 0);

    vuln();
    return 0;
}

__asm__(
    "   .thumb\n"
    "ldr    r0,     =0x6e69622f\n"
    "ldr    r1,     =0x68732f\n"
    "push   { r0, r1 }\n"
    "mov    r7,     #0x0b\n"
    "mov    r0,     sp\n"
    "eor    r1,     r1,     r1\n"
    "eor    r2,     r2,     r2\n"
    "svc    #0x00\n"
    "   .arm\n"
);