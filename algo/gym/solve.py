#!/usr/bin/env python3
from random import *
from base64 import b64decode
from pwn import *

rem = remote(args.HOST, args.PORT)

t = int(rem.recvline().decode())

for _ in range(t):
  print("tc", _)
  ars = rem.recvline().decode().split(" ")
  n = int(ars[0])
  k = int(ars[1])
  print(n, k)

  block_b64 = rem.recvline().decode()

  block_data = b64decode(block_b64)
  block = "".join(["{:08b}".format(x) for x in block_data])
  
  last = [0] * n
  for i in range(1, n):
    if block[i] == '0':
      last[i] = i
    else:
      last[i] = last[i - 1]
  steps = 0
  cur = 0
  ans = -1
  while cur != n - 1:
    nxt = last[min(cur + k, n - 1)]
    if nxt == cur:
      steps = -1
      break
    steps += 1
    cur = nxt
  ans = steps
  rem.sendline(str(ans).encode())

print(rem.recvline().decode())
