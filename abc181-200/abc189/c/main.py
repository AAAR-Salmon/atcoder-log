N = int(input())
A = list(map(int,input().split()))
ans = 0
for l in range(N):
	m = A[l]
	for r in range(l, N):
		m = min(m, A[r])
		ans = max(ans, m * (r - l + 1))
print(ans)
