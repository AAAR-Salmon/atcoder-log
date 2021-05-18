N = int(input())
dp = [0] * (24 * 12 + 2)

for _ in range(N):
	s, e = map(int,input().split('-'))
	dp[s // 100 * 12 + s % 100 // 5] += 1
	dp[e // 100 * 12 + (e % 100 + 4) // 5] -= 1
for i in range(24 * 12 + 1):
	dp[i + 1] += dp[i]

s = 0
for i in range(1, 24 * 12 + 2):
	if dp[i - 1] == 0 and dp[i] > 0:
		s = i
	if dp[i - 1] > 0 and dp[i] == 0:
		print(
			str(s // 12 * 100 + s % 12 * 5).zfill(4),
			'-',
			str(i // 12 * 100 + i % 12 * 5).zfill(4),
			sep='', flush=False)
