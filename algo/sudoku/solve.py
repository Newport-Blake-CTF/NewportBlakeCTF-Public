from pwn import *

rem = remote(args.HOST, args.PORT)

t = int(rem.recvline().decode())

for _ in range(t):
  print("tc", _)
  n = int(rem.recvline().decode())
  ar = rem.recvline().decode().split(" ")
  for i in range(n):
    ar[i] = int(ar[i]) - 1
  arr = []
  for i in range(n):
    a = [0] * n
    arr.append(a)
  top = 2 * ((n - 1) // 2) + 1
  for i in range(top):
    start = (2 * i) % top
    for j in range(top):
      arr[i][j] = start
      start = start - 1
      if start < 0:
        start = top - 1
  if n % 2 == 0:
    arr[n - 1][n - 1] = n - 1
    for i in range(n - 1):
      arr[n - 1][i] = (i + n - 3) % (n - 1)
      arr[i][n - 1] = (i + n - 2) % (n - 1)
      arr[i][(i + 1) % (n - 1)] = n - 1
  at = []
  for j in range(n):
    at.append(j)
  for i in range(n):
    k = 0
    for j in range(n):
      if at[j] == i:
        k = j
        break
    k2 = ar[i]
    at[k], at[k2] = at[k2], at[k]
    for j in range(n):
      arr[k][j], arr[k2][j] = arr[k2][j],  arr[k][j]
  for i in range(n):
    for j in range(n):
      rem.send(str(arr[j][i] + 1).encode())
      if j < n - 1:
        rem.send(" ".encode())
    rem.sendline()

print(rem.recvline().decode())
