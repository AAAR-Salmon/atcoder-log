N=int(input())
A=list(map(int,input().split()))
K=1
for a in A:
  if a == K:
    K += 1
if K == 1:
  print(-1)
else:
  print(N-K+1)
