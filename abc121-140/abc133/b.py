import math
N,D=map(int,input().split())
X=[None]*N
cnt=0
for i in range(N):
  X[i]=list(map(int,input().split()))
for i in range(N-1):
  for j in range(i+1,N):
    d2=0
    for k in range(D):
      d2 += (X[i][k] - X[j][k]) ** 2
    if int(math.sqrt(d2)) ** 2 == d2:
      cnt += 1
print(cnt)
