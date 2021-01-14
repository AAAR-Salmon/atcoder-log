N,H,W=map(int,input().split())
ans=0
for _ in range(N):
	a,b=map(int,input().split())
	if a >= H and b >= W:
		ans += 1
print(ans)
