from sys import exit
N=int(input())
H=list(map(int,input().split()))
# 極大から次の極小までに2以上下がったらアウト
inc=0
for i in range(N - 1):
  if H[i + 1] - H[i] > 0:
    inc = 1
  else:
    if inc > 0:
      inc = 0
    inc += H[i + 1] - H[i]
    if inc < -1:
      print('No')
      exit()
print('Yes')
