import random
import struct

flag = b"L3f7_f0rw4Rd_r1gh7_rIghT_l3FT_1n_RigH7_b4cK_return".split(b"_")
nums = [4, 7, 2, 0, 3, 6, 5, 1, 8]

# basically you just reverse each operation shown below

i = 0
word = flag[nums[i]]
print(word)
for c in word:
    print(c ^ 0x68, end=" ")
print()

i += 1
word = flag[nums[i]]
print(word)
for c in word:
    n = 0
    for j in range(4):
        n |= (c & 0x3) << (j * 4 + 2)
        c >>= 2
    print(n, end=" ")
print()

i += 1
word = flag[nums[i]]
print(word)
r = [random.randint(0, 0xffff)]
for c in word:
    r.append(random.randint(0, 0xffff))
    print(c * r[-1] + r[-2], end=" ")   
print(r)

i += 1
word = flag[nums[i]]
threestep = list(word) + [ord('_')]
print(threestep)
print(word)

i += 1
word = flag[nums[i]]
s = [0]
for j, c in enumerate(word):
    s.append(s[-1] + c * 128 + threestep[j])

print(s[1:])
print(word)

i += 1
word = flag[nums[i]]
for j, c in enumerate(word):
    j += 3
    c = (c >> j) | (c << (32 - j)) & 0xffffffff
    print(c, end=", ")
print()
print(word)

i += 1
word = flag[nums[i]]
h = struct.unpack("<H", word)[0]
while h:
    b = h & (~h + 1)
    print(b, end=", ")
    h ^= b
print()

i += 1
word = flag[nums[i]] + b'_'
f = struct.unpack("<d", word)[0]
print(f)
print(word)

i += 1
word = flag[nums[i]]
for c in word:
    print(c ^ 0xc3, end=", ")
print()
print(word)