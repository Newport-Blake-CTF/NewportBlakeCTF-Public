#!/usr/local/bin/python
from random import *
from flag import flag

MOD = 10**9 + 7

def p(x, y):
    if y == 0:
        return 1
    b = p(x, y >> 1)
    b = (b * b) % MOD
    if y & 1:
        b = (b * x) % MOD
    return b

def inv(x):
    return p(x, MOD - 2)

t = 10

print(t)

min_n = 50000
min_m = 10 ** 8

for _ in range(t):
  n = randint(min_n, 2 * min_n)
  m = randint(min_m, 2 * min_m)
  print(str(2 * n) + " " + str(m))
  
  rep = randint(_ * (n // t) + 1, (_ + 1) * (n // t))
  rep = min(rep, n)
  rep = max(rep, 1)
  while n % rep > 0:
    rep -= 1
  
  s = ""
  fs = ""
  for j in range(rep):
    s += str(randint(0, 1))
  for j in range(0, n // rep):
    fs += s
  
  print(fs)

  fs = fs + fs
  ones = fs.count('1')
  ans = 0
  n = 2 * n

  if ones == 0:
      ans = m % MOD
  else:
      burnside = [0] * (n + 1)
      f = 0
      for i in range(1, n + 1):
          if n % i != 0:
              continue
          first = fs[:i]
          works = True
          for j in range(0, n, i):
            for k in range(0, i):
              if fs[j + k] != first[k]:
                works = False
                break
          if not works:
              continue
          if ones % (n // i) != 0:
              continue
          if f == 0:
              f = i
          todo = ones // (n // i)
          num = (p(m, todo) - burnside[todo] + MOD) % MOD
          for j in range(todo * 2, n + 1, todo):
              burnside[j] = (burnside[j] + num) % MOD
          assert i % f == 0
          ans = (ans + num * inv(i // f)) % MOD
  
  a = int(input())
  if a != ans:
    print("WA")
    exit()

print("AC", flag)
