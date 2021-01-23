N = int(input())
S = [input() for _ in range(N)]
dp = [0] * (N+1)
dp[1] = 1
for i in range(1, N+1):
	if S[i-1] == 'AND':
		dp[i] = dp[i-1]
	else:
		dp[i] = pow(2, i) + dp[i-1]
print(dp[N] + 1)
