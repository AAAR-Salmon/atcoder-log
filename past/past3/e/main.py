from itertools import chain

N, M, Q = map(int, input().split())
adj = [[] for _ in range(N + 1)]
for _ in range(M):
	u, v = map(int, input().split())
	adj[u].append(v)
	adj[v].append(u)
c = list(chain([0], map(int, input().split())))
for _ in range(Q):
	s = tuple(map(int, input().split()))
	print(c[s[1]])
	if s[0] == 1:
		for i in adj[s[1]]:
			c[i] = c[s[1]]
	else:
		c[s[1]] = s[2]
