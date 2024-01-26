    .global _start

_start:
    mov r0, #0x6873
    push { r0 }
    mov r8, sp
    mov r9, #2
    push { r8, r9 }
    mov r0, #0x12
    mov r1, sp
    hlt #0xf000    
