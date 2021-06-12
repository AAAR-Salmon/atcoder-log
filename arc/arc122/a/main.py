MOD = 1000000007

N = int(input())
A = list(map(int, input().split()))

dp = [[0] * 2 for _ in range(N)]
cnt = [[0] * 2 for _ in range(N)]
dp[0][0] = A[0]
cnt[0][0] = 1
for i in range(1, N):
	cnt[i][0] = (cnt[i - 1][0] + cnt[i - 1][1]) % MOD
	cnt[i][1] = cnt[i - 1][0]
	dp[i][0] = (dp[i - 1][0] + dp[i - 1][1] + A[i] * cnt[i][0]) % MOD
	dp[i][1] = (dp[i - 1][0] - A[i] * cnt[i][1]) % MOD

print((dp[-1][0] + dp[-1][1]) % MOD)
