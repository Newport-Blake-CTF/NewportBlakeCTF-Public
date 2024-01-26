from z3 import *

enc = [902, 764, 141, 454, 207, 51, 532, 1013, 496, 181, 562, 342]
alpha = " zvtwrca57n49u2by1jdqo6g0ksxfi8pelmh3"

key = "isaac newton"
key = [alpha.index(c) for c in key]

s = Solver()
flag = [Int(f"flag_{i}") for i in range(len(enc))]

for i in range(len(enc)):
    j = ((i + 1) * (i + 1) + key[i]) % len(enc)
    s.add(flag[i] * flag[j] + key[i] * key[j] == enc[i])

s.check()
m = s.model()
print("".join([alpha[m[flag[i]].as_long()] for i in range(len(enc))]))