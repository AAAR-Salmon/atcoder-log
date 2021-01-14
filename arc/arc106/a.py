from sys import exit
N=int(input())
A=B=1
while 3 ** A <= N:
  B = 1
  while 3 ** A + 5 ** B <= N:
    if 3 ** A + 5 ** B == N:
      print(A, B)
      exit()
    B += 1
  A += 1
print(-1)
