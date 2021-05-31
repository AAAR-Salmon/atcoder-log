N=int(input())
H=list(map(int,input().split()))
ans=0
for i in range(N):
  ov=True
  for j in range(i):
    if H[j] > H[i]:
      ov=False
      break
  if ov:
    ans+=1
print(ans)
