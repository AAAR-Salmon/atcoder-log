from collections import deque
H, W = map(int, input().split())
s = [input() for _ in range(H)]
INF = 2500
dp = [[INF] * W for _ in range(H)]
if s[0][0] == '#':
	print(-1)
	exit(0)
dp[0][0] = 0
q = deque([(0, 0)])
while q:
	y, x = q.popleft()
	for dy, dx in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
		if not (0 <= y+dy < H and 0 <= x+dx < W) or s[y+dy][x+dx] == '#' or dp[y+dy][x+dx] < INF:
			continue
		dp[y+dy][x+dx] = dp[y][x] + 1
		q.append((y+dy, x+dx))
if dp[H-1][W-1] == INF:
	print(-1)
else:
	print(sum(s[i].count('.') for i in range(H)) - dp[H-1][W-1] - 1)
