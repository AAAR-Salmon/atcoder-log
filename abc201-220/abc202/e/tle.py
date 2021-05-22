from collections import deque

N = int(input())
parent = [0] * (N + 1)
children = [[] for _ in range(N + 1)]
P = list(map(int,input().split()))
for i in range(2, N + 1):
	parent[i] = P[i - 2]
	children[P[i - 2]].append(i)

depth = [0] * (N + 1)
depth[0] = -1
depth_to_node = [[] for _ in range(N)]
depth_to_node[0].append(1)
q = deque([(1, 0)])
while q:
	n, d = q.popleft()
	for c in children[n]:
		depth[c] = d + 1
		depth_to_node[d + 1].append(c)
		q.append((c, d + 1))

Q = int(input())
ancestor = [set([i]) for i in range(N + 1)]
for _ in range(Q):
	U, D = map(int,input().split())
	ans = 0
	for v in depth_to_node[D]:
		n = v
		while depth[n] >= 0:
			ancestor[v].add(n)
			if U in ancestor[n]:
				ans += 1
				break
			n = parent[n]
	print(ans, flush=False)


