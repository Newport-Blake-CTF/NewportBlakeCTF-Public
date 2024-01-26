from pwn import *

HOST=
PORT=

p = remote(HOST, PORT)

# have fun :D

p.interactive()