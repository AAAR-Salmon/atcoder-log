import numpy as np
from collections import deque

INF = 1 << 60
dpos4 = ((-1, 0), (0, -1), (0, 1), (1, 0))

H, W = map(int, input().split())

c = [None] * H
for i in range(H):
	c[i] = line = input()
	if 's' in line:
		Sx, Sy = i, line.index('s')
	if 'g' in line:
		Gx, Gy = i, line.index('g')

dp = np.full((H, W), INF, np.int64)
dp[Sx, Sy] = 0

q = deque([(Sx, Sy)])

while q:
	x, y = q.popleft()
	for dx, dy in dpos4:
		tx, ty = x + dx, y + dy
		if not (0 <= tx < H and 0 <= ty < W):
			continue
		if dp[tx, ty] != INF:
			continue
		if c[tx][ty] == '#':
			dp[tx, ty] = dp[x, y] + 1
			q.append((tx, ty))
		else:
			dp[tx, ty] = dp[x, y]
			q.appendleft((tx, ty))

print('YES' if dp[Gx, Gy] <= 2 else 'NO')
