N=int(input())
A=list(map(lambda s:int(s)-1,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))
ans=0
p=-2
for a in A:
  ans += B[a]
  if p + 1 == a:
    ans += C[a - 1]
  p = a
print(ans)
