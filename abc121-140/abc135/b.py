N=int(input())
p=list(map(int,input().split()))
q=sorted(p)
cnt=0
for i in range(N):
  if p[i] != q[i]:
    cnt += 1
print('YES' if cnt <= 2 else 'NO')
