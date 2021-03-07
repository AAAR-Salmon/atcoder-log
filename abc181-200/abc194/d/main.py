N = int(input())
dp = [0] * (N + 1)
dp[1] = 0
for i in range(2, N + 1):
	dp[i] = dp[i - 1] + 1 + (i - 1) / (N - i + 1)
print(dp[N])
