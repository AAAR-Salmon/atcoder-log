MOD = 998244353

N,K = map(int,input().split())
L = [None] * K
R = [None] * K
for i in range(K):
	L[i],R[i] = map(int,input().split())

dp = [0] * N
dp[0] = 1
dp[1] = -1

for i in range(N):
	if i > 0:
		dp[i] += dp[i-1]
		dp[i] %= MOD
	for j in range(K):
		if i+L[j] < N:
			dp[i+L[j]] += dp[i]
			if i+R[j]+1 < N:
				dp[i+R[j]+1] -= dp[i]
print(dp[N-1])
