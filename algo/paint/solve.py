from pwn import *

rem = remote(args.HOST, args.PORT)

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

t = int(rem.recvline().decode())

for _ in range(t):
  print("tc", _)
  n, m = map(int, rem.recvline().decode().split(" "))
  # print(n, m)
  s = rem.recvline().decode().strip()
  s = s + s
  ones = s.count('1')
  ans = 0

  if ones == 0:
      rem.sendline(str(m % MOD).encode())
  else:
      burnside = [0] * (n + 1)
      f = 0
      for i in range(1, n + 1):
          if n % i != 0:
              continue
          first = s[:i]
          works = True
          for j in range(0, n, i):
            for k in range(0, i):
              if s[j + k] != first[k]:
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

      rem.sendline(str(ans).encode())

print(rem.recvline().decode())
