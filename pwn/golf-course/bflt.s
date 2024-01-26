    .global _start

    .equ VERSION, (4 | ('h' << 32) | ('s' << 40)) 
    .equ FLAG_RAM, (1)

    /*
    .macro swap arg
        .word (\arg >> 24) | (\arg >> 16 & 0xff << 8) | (\arg >> 8 & 0xff << 16) | (\arg << 24)
    .endm */
    .macro swap arg
        .8byte (\arg >> 56) | (((\arg >> 48) & 0xff) << 8) | (((\arg >> 40) & 0xff) << 16) | (((\arg >> 32) & 0xff) << 24) | (((\arg >> 24) & 0xff) << 32) | (((\arg >> 16) & 0xff) << 40) | (((\arg >> 8) & 0xff) << 48) | (\arg << 56)
    .endm

.magic:
    .byte 'b', 'F', 'L', 'T'
.version:
    swap VERSION
.entry:
    swap (_start - .magic)
.dstart:
    .8byte 0x000005500000006
.dend:
    .8byte 0x000005500000006
.bend:
_cmd:
    .8byte 0x000005500000006
.stacksz:
    .4byte 0
_start:
    add x0, x0, #0x12
.rstart:
    adr x1, _cmd
    hlt #0xf000
.rcount:
    .4byte 0
.flags:
.build_date:
.end:
