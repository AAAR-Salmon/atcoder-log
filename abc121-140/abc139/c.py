N=int(input())
H=list(map(int,input().split()))
ans=0
c=0
for i in range(N-1):
  if H[i] >= H[i+1]:
    c += 1
  else:
    if c > ans:
      ans = c
    c = 0
if c > ans:
  ans = c
print(ans)
