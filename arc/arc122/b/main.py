N = int(input())
A = sorted(map(int,input().split()))
S = [0] * (N + 1)

for i in range(N):
	S[i + 1] = S[i] + A[i]

# E[x + A[i] - min(A[i], 2x)]
# = x + E[A[i]] - E[min(A[i], 2x)]

ans = 1e18
for a in A:
	x = a / 2
	l, r = -1, N
	while r - l > 1:
		m = (l + r) // 2
		if A[m] <= a:
			l = m
		else:
			r = m
	ans = min(ans, x + S[N] / N - (S[l] + 2 * x * (N - l)) / N)
print(ans)
