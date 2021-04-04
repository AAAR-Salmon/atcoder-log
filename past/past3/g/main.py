from collections import deque

INF = 160000
dpos = [(1, 1), (0, 1), (-1, 1), (1, 0), (-1, 0), (0, -1)]

N, X, Y = map(int, input().split())
X += 201
Y += 201
exist_barrier = [[False] * 403 for _ in range(403)]
for i in range(N):
	x, y = map(int, input().split())
	exist_barrier[x + 201][y + 201] = True
mint = [[INF] * 403 for _ in range(403)]
q = deque([(201, 201)])
mint[201][201] = 0
while q:
	cx, cy = q.popleft()
	ct = mint[cx][cy]
	for dx, dy in dpos:
		if not (0 <= cx + dx < 403 and 0 <= cy + dy < 403):
			continue
		if exist_barrier[cx + dx][cy + dy]:
			continue
		if mint[cx + dx][cy + dy] != INF:
			continue
		mint[cx + dx][cy + dy] = ct + 1
		if (cx + dx, cy + dy) == (X, Y):
			print(ct + 1)
			exit(0)
		q.append((cx + dx, cy + dy))
print(-1)
