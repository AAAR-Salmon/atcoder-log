N,M,C=map(int,input().split())
B=list(map(int,input().split()))
A=[list(map(int,input().split())) for i in range(N)]
cnt=0
for a in A:
  sum=0
  for i in range(M):
    sum += a[i]*B[i]
  if sum + C > 0:
    cnt += 1
print(cnt)
