#include <stdio.h>
#include <stdbool.h>
#include <stdint.h>
#include <unistd.h>

extern void challenge(uint8_t *data, size_t len);

#define SIZE 0x10000

char banner[] = "\
██████╗ ██╗      ██████╗  ██████╗██╗  ██╗    \n\
██╔══██╗██║     ██╔═══██╗██╔════╝██║ ██╔╝    \n\
██████╔╝██║     ██║   ██║██║     █████╔╝     \n\
██╔══██╗██║     ██║   ██║██║     ██╔═██╗     \n\
██████╔╝███████╗╚██████╔╝╚██████╗██║  ██╗    \n\
╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝    \n\
                                             \n\
 ██████╗██╗  ██╗ █████╗ ██╗███╗   ██╗██████╗ \n\
██╔════╝██║  ██║██╔══██╗██║████╗  ██║╚════██╗\n\
██║     ███████║███████║██║██╔██╗ ██║  ▄███╔╝\n\
██║     ██╔══██║██╔══██║██║██║╚██╗██║  ▀▀══╝ \n\
╚██████╗██║  ██║██║  ██║██║██║ ╚████║  ██╗   \n\
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝  ╚═╝   \n\
";

int main() {
    int processed = 0;
    int numb;

    setbuf(stdout, NULL);
    setbuf(stderr, NULL);

    printf("%s", banner);
    
    printf("I'll be nice and give you a leak.\n");
    printf("leak: %p\n", (void *)&challenge);

    uint8_t file[SIZE];
    printf("ELF file: ");

    while (processed < SIZE) {
        numb = read(0, file + processed, SIZE-processed);
        if (numb > 0) {
            processed += numb;
        }
    }

    challenge(file, SIZE);
}