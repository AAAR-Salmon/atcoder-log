N,K=map(int,input().split())
h=list(map(int,input().split()))
cnt=0
for v in h :
  if v >= K: cnt += 1
print(cnt)
