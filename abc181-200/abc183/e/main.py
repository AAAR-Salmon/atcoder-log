MOD = 1_000_000_007

H, W = map(int, input().split())
grid = [input() for _ in range(H)]
dp, dp1, dp2, dp3 = (tuple([0] * (W + 1) for _ in range(H + 1)) for _ in range(4))
dp[1][1] = 1
for i in range(1, H + 1):
	for j in range(1, W + 1):
		if grid[i - 1][j - 1] == '#':
			continue
		dp[i][j] += dp1[i - 1][j] + dp2[i - 1][j - 1] + dp3[i][j - 1]
		dp[i][j] %= MOD
		dp1[i][j] = (dp1[i - 1][j] + dp[i][j]) % MOD
		dp2[i][j] = (dp2[i - 1][j - 1] + dp[i][j]) % MOD
		dp3[i][j] = (dp3[i][j - 1] + dp[i][j]) % MOD

print(dp[H][W])
