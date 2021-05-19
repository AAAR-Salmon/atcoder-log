N, M = map(int, input().split())
edge = [[False] * N for _ in range(N)]

for i in range(N):
	edge[i][i] = True

for _ in range(M):
	x, y = map(lambda x: int(x) - 1, input().split())
	edge[x][y] = True
	edge[y][x] = True

ans = 0
for f in range(1 << N):
	satisfiable = True
	for i in range(N):
		if f >> i & 1 == 0:
			continue
		for j in range(i):
			if f >> j & 1 and not edge[i][j]:
				satisfiable = False
				break
		if not satisfiable:
			break
	if satisfiable:
		f = f - (f >> 1 & 0x5555)
		f = (f & 0x3333) + (f >> 2 & 0x3333)
		f += f >> 4
		f += f >> 8
		ans = max(ans, f & 0xf)
print(ans)
