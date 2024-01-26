key = b'0NL1N3'

mat = [list(key)] * 6
for i in range(6):
    mat[i] = mat[i][i:] + mat[i][:i]

from numpy import array

mat = array(mat)
sqr = mat @ mat

# reshape to 1D array
print(list(mat.reshape(36)))

flag = b"wh0_kn3w_ch4tGPT_w0uld_write_5uch_g00d_c0de?_jk_th15_is_h0t_g4rbo!"

chunks = [flag[i:i+6] for i in range(0, len(flag), 6)]

enc = []
for chunk in chunks:
    print(chunk)
    chunk = array(list(chunk))
    print(mat @ chunk)
    enc += list(mat @ chunk)

print(enc)