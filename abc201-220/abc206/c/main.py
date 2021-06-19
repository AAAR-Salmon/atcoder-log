from collections import defaultdict

N = int(input())
A = defaultdict(lambda: 0)

for a in map(int, input().split()):
	A[a] += 1

ans = 0
dp = [0] * (len(A) + 1)
for i, a in enumerate(A.keys()):
	ans += dp[i] * A[a]
	dp[i + 1] = dp[i] + A[a]

print(ans)