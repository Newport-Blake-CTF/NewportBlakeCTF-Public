#!/usr/local/bin/python
from random import *
from flag import flag

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

t = 1

print(t)

minqn = 50000

for i in range(t):
  n = minqn
  arr = []
  print(n)
  for j in range(n):
    x = randint(1, 1000000000)
    arr.append(x)
    print(x, end="")
    if j < n - 1:
      print(" ", end="")
  str_input = []
  print()
  for j in range(n):
    x = randint(0, 1)
    print(x, end="")
    str_input.append(str(x))
  str_input = ''.join(str_input)
  print()
  q = minqn
  print(q)
  exp = 0
  qs = []
  ps = []
  for j in range(q):
    x = randint(1, 2)
    y = randint(1, n)
    z = randint(y, n)
    qs.append((x, y, z))
    ps.append(str(x))
    ps.append(str(y))
    ps.append(str(z))
    if x == 2:
      exp += 1
  print(' '.join(ps))
  ans = []

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
        ans.append(0)
      else:
        ans.append(inf - 69 - mx)
  
  for j in range(exp):
    num = int(input())
    if ans[j] != num:
      print("WA")
      exit()

print("AC", flag)
