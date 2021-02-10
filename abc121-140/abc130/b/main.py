N,X=map(int,input().split())
L=list(map(int,input().split()))
s=[0]*N
s[0]=L[0]
for i in range(N-1):
  s[i+1]=s[i]+L[i+1]
cnt=1
for d in s:
  if d > X:
    break
  cnt += 1
print(cnt)
