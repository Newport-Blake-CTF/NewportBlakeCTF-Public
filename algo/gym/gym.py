#!/usr/local/bin/python
from random import *
from base64 import b64encode
from flag import flag

t = 20

print(t)

min_n = 50000

for _ in range(t):
  n = randint(min_n, 2 * min_n)
  k = randint(1, int(min_n // (5 * (10 ** (_ / 7)))))
  k = max(min(k, n - 1), 1)
  print(str(n) + " " + str(k))
  block = ""
  for i in range(n):
    x = randint(0, 1)
    if i == 0 or i == n - 1:
      block += "0"
      print(0, end="")
    else:
      print(x, end="")
      block += str(x)
  print()

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
  a = int(input())
  if a != ans:
    print("WA")
    exit()

print("AC", flag)
