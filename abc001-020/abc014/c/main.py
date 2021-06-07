N = int(input())
dp = [0] * 1000002
for _ in range(N):
	a, b = map(int,input().split())
	dp[a] += 1
	dp[b + 1] -= 1

for i in range(1000001):
	dp[i + 1] += dp[i]

print(max(dp))
