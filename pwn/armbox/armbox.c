#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/mman.h>

void filter() {
    __asm__ __volatile__(
        "push   { r7 }\n"
        "mov    r7,     #0x6969\n"
        "svc    #0\n"
        "pop    { r7 }\n"
    );
}

#define BYTES 0x10000

int main() {
    setbuf(stdout, NULL);
    
    printf("welcome to the secure armbox computing facility.\n");

    char *code = mmap(NULL, BYTES, PROT_READ | PROT_WRITE | PROT_EXEC, MAP_PRIVATE | MAP_ANON, -1, 0);
    printf("program: ");

    int processed = 0;
    while (processed != BYTES) {
        int status = read(0, code + processed, BYTES - processed);
        if (status < 0) {
            perror("failed");
            exit(0);
        }
        processed += status;
    }

    filter();

    ((void(*)(void))code)();
}