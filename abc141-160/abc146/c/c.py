A,B,X=map(int,input().split())
ans=0
for d in range(1,11):
  N=(X-B*d)//A
  if N >= 10**(d-1): ans = min(N, 10**d-1, 1000000000)
print(ans)
