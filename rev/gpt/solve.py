mat = """0000dedb              var_308[0] = 0x62a2;
0000dee7              var_308[1] = 0x5c5c;
0000def3              var_308[2] = 0x5c43;
0000deff              var_308[3] = 0x6030;
0000df0b              var_308[4] = 0x5c43;
0000df17              var_308[5] = 0x5c5c;
0000df23              var_308[6] = 0x5c5c;
0000df2f              var_308[7] = 0x62a2;
0000df3b              var_308[8] = 0x5c5c;
0000df47              var_308[9] = 0x5c43;
0000df53              var_308[0xa] = 0x6030;
0000df5f              var_308[0xb] = 0x5c43;
0000df6b              var_308[0xc] = 0x5c43;
0000df77              var_308[0xd] = 0x5c5c;
0000df83              var_308[0xe] = 0x62a2;
0000df8f              var_308[0xf] = 0x5c5c;
0000df9b              var_308[0x10] = 0x5c43;
0000dfa7              var_308[0x11] = 0x6030;
0000dfb3              var_308[0x12] = 0x6030;
0000dfbf              var_308[0x13] = 0x5c43;
0000dfcb              var_308[0x14] = 0x5c5c;
0000dfd7              var_308[0x15] = 0x62a2;
0000dfe3              var_308[0x16] = 0x5c5c;
0000dfef              var_308[0x17] = 0x5c43;
0000dffb              var_308[0x18] = 0x5c43;
0000e007              var_308[0x19] = 0x6030;
0000e013              var_308[0x1a] = 0x5c43;
0000e01f              var_308[0x1b] = 0x5c5c;
0000e02b              var_308[0x1c] = 0x62a2;
0000e037              var_308[0x1d] = 0x5c5c;
0000e043              var_308[0x1e] = 0x5c5c;
0000e04f              var_308[0x1f] = 0x5c43;
0000e05b              var_308[0x20] = 0x6030;
0000e067              var_308[0x21] = 0x5c43;
0000e073              var_308[0x22] = 0x5c5c;
0000e07f              var_308[0x23] = 0x62a2;"""

mat = [int(line.split(" = ")[1].split(";")[0], 16) for line in mat.split("\n")]
import numpy as np

mat = np.array(mat)
mat = mat.reshape(6, 6)
# square rooting
# you can do this with the fixed values and lin alg but :shrug: this is eaiser
import z3

s = z3.Solver()
key = [z3.BitVec(f"key_{i}", 32) for i in range(6)]
for i in range(6):
    s.add(32 <= key[i])
    s.add(key[i] < 127)

s.add(key[0] == b'0'[0])
s.add(key[1] == b'N'[0])

key_mat = []
for i in range(6):
    key_mat.append(key[i:] + key[:i])

# mat mul
for i in range(6):
    for j in range(6):
        sum = z3.Sum([key_mat[i][k] * key_mat[k][j] for k in range(6)])
        s.add(sum == int(mat[i, j]))

print(s.check())
m = s.model()
key = [m[key[i]].as_long() for i in range(6)]
print(bytes(key))

mat = []
for i in range(6):
    mat.append(key[i:] + key[:i])

mat = np.array(mat)
# mat = mat @ mat

data = open('gpt', 'rb').read()
# load static array

start = 0x54470 # start of array
D = []

import struct
for i in range(66):
    D.append(struct.unpack("<Q", data[start + i * 8:start + (i + 1) * 8])[0])

flag = []
for i in range(0, len(D), 6):
    flag += list(np.linalg.solve(mat, D[i:i+6]))
    
flag = bytes([round(i) for i in flag])
print(flag)