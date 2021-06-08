from collections import deque

N = int(input())
edges = [[] for _ in range(N)]
for _ in range(N - 1):
	x, y = map(lambda x: int(x) - 1, input().split())
	edges[x].append(y)
	edges[y].append(x)

depth = [-1] * N
depth[0] = 0
parent = [[] for _ in range(N)]
q = deque([0])
while q:
	p = q.pop()
	for n in edges[p]:
		if depth[n] != -1:
			continue
		depth[n] = depth[p] + 1
		parent[n].append(p)
		parent_n_k = p
		k = 0
		d = depth[p]
		while d >= 1 << k:
			parent[n].append(parent[parent_n_k][k])
			parent_n_k = parent[n][-1]
			d -= 1 << k
			k += 1
		q.append(n)

Q = int(input())
for _ in range(Q):
	a, b = map(lambda x: int(x) - 1, input().split())
	x, y = a, b
	if depth[x] < depth[y]:
		x, y = y, x
	dd = depth[x] - depth[y]
	k = 0
	while dd > 0:
		if dd >> k & 1:
			x = parent[x][k]
			dd -= 1 << k
		k += 1

	if x == y:
		print(depth[a] + depth[b] - depth[x] * 2 + 1)
		continue

	for i in range(16, -1, -1):
		if i >= len(parent[x]):
			continue
		if parent[x][i] != parent[y][i]:
			x = parent[x][i]
			y = parent[y][i]

	print(depth[a] + depth[b] - depth[x] * 2 + 3)
