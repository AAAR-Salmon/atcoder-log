L = int(input())
dp = [0] * (L-12+1)
dp[0] = 1
for i in range(12):
	for l in range(1,L-12+1):
		dp[l] = dp[l]+dp[l-1]
print(dp[L-12])
