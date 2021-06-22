INF = 1 << 60

N, M = map(int, input().split())
S = input()
dp = [-1] * (N + 1)
pos = N
done = N

while pos:
	for nextpos in range(max(0, pos - M), done + 1):
		if nextpos >= done:
			print(-1)
			exit(0)
		if S[nextpos] == '1':
			continue
		dp[nextpos] = pos
		done = max(pos - M, 0)
		pos = nextpos
		break

ans = []
while dp[pos] != -1:
	ans.append(dp[pos] - pos)
	pos = dp[pos]

print(*ans)
