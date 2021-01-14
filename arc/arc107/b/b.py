N,K=map(int,input().split())
K=abs(K)
ans=0
sl=2 * N - K
for s in range(2, sl+1):
	ans += min(K + s - 1, 2 * N - K - s + 1) * min(s - 1, 2 * N - s + 1)
print(ans)
