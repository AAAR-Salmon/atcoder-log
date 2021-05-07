MOD = 1_000_000_007

N, K = map(int, input().split())
X = max(N - K + 1, K - 1)

comb = [[0] * (K + 1) for _ in range(X + 1)]
comb[0][0] = 1

for i in range(1, X + 1):
	comb[i][0] = 1
	for j in range(1, K + 1):
		comb[i][j] = (comb[i - 1][j] + comb[i - 1][j - 1]) % MOD

for i in range(1, K + 1):
	print(comb[N - K + 1][i] * comb[K - 1][i - 1] % MOD)
