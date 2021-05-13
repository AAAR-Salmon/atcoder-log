MOD = 1_000_000_007

S = input()
N = len(S)
M = 13
dp = [[0] * M for _ in range(N+1)]
dp[0][0] = 1

for i in range(N):
	for d in (range(10) if S[i] == '?' else (int(S[i]),)):
		for j in range(M):
			dp[i + 1][(j * 10 + d) % M] += dp[i][j]
			dp[i + 1][(j * 10 + d) % M] %= MOD

print(dp[-1][5])
