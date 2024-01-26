alpha = " zvtwrca57n49u2by1jdqo6g0ksxfi8pelmh3"

key = "isaac newton"
key = [alpha.index(c) for c in key]

flag = "nbctf{12lett3rf149}"

assert flag.startswith("nbctf{") and flag.endswith("}")

flag = flag[6:-1]
flag = [alpha.index(c) for c in flag]
print(flag)

assert len(flag) == len(key)

enc = []
for i in range(len(flag)):
    j = ((i + 1) * (i + 1) + key[i]) % len(flag)
    print(i, j)
    enc.append(flag[i] * flag[j] + key[i] * key[j])

print(enc)