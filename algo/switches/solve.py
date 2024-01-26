from random import *
from pwn import *

inf = 2000000000

class MLST:
    def __init__(self, nn):
        self.nn = nn
        self.t = [(inf, -inf)] * (4 * nn)
        self.lz = [False] * (4 * nn)

    def build(self, v, l, r, arr):
        if l == r:
            self.t[v] = (arr[l], arr[l])
            return self.t[v]
        m = (l + r) // 2
        _l = self.build(2 * v, l, m, arr)
        _r = self.build(2 * v + 1, m + 1, r, arr)
        self.t[v] = (min(_l[0], _r[0]), max(_l[1], _r[1]))
        return self.t[v]

    def build_tree(self, arr):
        self.build(1, 0, self.nn - 1, arr)

    def push(self, v, l, r):
        if not self.lz[v]:
            return
        self.lz[v] = False
        if l == r:
            return
        self.lz[2 * v] = not self.lz[2 * v]
        self.lz[2 * v + 1] = not self.lz[2 * v + 1]
        self.t[2 * v] = (-self.t[2 * v][1], -self.t[2 * v][0])
        self.t[2 * v + 1] = (-self.t[2 * v + 1][1], -self.t[2 * v + 1][0])

    def flip(self, v, tl, tr, l, r):
        if l > r:
            return self.t[v]
        if tl == l and tr == r:
            self.lz[v] = not self.lz[v]
            return (-self.t[v][1], -self.t[v][0])
        self.push(v, tl, tr)
        m = (tl + tr) // 2
        _l = self.flip(2 * v, tl, m, l, min(m, r))
        _r = self.flip(2 * v + 1, m + 1, tr, max(m + 1, l), r)
        self.t[v] = (min(_l[0], _r[0]), max(_l[1], _r[1]))
        return self.t[v]

    def flip_range(self, l, r):
        self.flip(1, 0, self.nn - 1, l, r)

    def query_max(self, v, tl, tr, l, r):
        if l > r:
            return -inf
        if tl == l and tr == r:
            return self.t[v][1]
        self.push(v, tl, tr)
        m = (tl + tr) // 2
        return max(self.query_max(2 * v, tl, m, l, min(m, r)), self.query_max(2 * v + 1, m + 1, tr, max(m + 1, l), r))

    def query_max_range(self, l, r):
        return self.query_max(1, 0, self.nn - 1, l, r)

rem = remote(args.HOST, args.PORT)

t = int(rem.recvline().decode())


for i in range(t):
  print("tc", i)
  n = int(rem.recvline().decode())
  print(n)
  arr = []
  xs = rem.recvline().decode().split(" ")
  for j in range(n):
    x = int(xs[j])
    arr.append(x)
  str_input = rem.recvline().decode()
  q = int(rem.recvline().decode())
  exp = 0
  print(q)
  qs = []
  for j in range(q):
    ar = rem.recvline().decode().split(" ")
    x = int(ar[0])
    y = int(ar[1])
    z = int(ar[2])
    qs.append((x, y, z))
    if x == 2:
      exp += 1  

  for i in range(n):
    arr[i] = inf - 69 - arr[i]
  mlst = MLST(n)
  mlst.build_tree(arr)
  for _ in range(q):
    t, l, r = qs[_]
    l -= 1
    r -= 1
    if t == 1:
      mlst.flip_range(l, r)
    else:
      mx = mlst.query_max_range(l, r)
      if mx < 0:
        rem.sendline("0".encode())
      else:
        rem.sendline(str(inf - 69 - mx).encode())
  

print(rem.recvline().decode())
