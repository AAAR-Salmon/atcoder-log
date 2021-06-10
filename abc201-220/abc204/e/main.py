from heapq import heappush, heappop

INF = 1 << 60


def isqrt(n: int) -> int:
	l, r = -1, n + 1
	while r - l > 1:
		m = (l + r) // 2
		if m * m <= n:
			l = m
		else:
			r = m
	return l


N, M = map(int, input().split())
edges = [[] for _ in range(N + 1)]
for i in range(M):
	a, b, c, d = map(int, input().split())
	edges[a].append((b, c, d))
	edges[b].append((a, c, d))

dp = [INF] * (N + 1)
dp[1] = 0
h = [(0, 1)]
while h:
	t, fr = heappop(h)
	if t > dp[fr]:
		continue
	for to, c, d in edges[fr]:
		s = t + c + d // (t + 1)
		rd = isqrt(d)
		for i in range(max(t, rd - 1), rd + 2):
			s = min(s, i + c + d // (i + 1))
		if s < dp[to]:
			dp[to] = s
			heappush(h, (s, to))

print(-1 if dp[N] == INF else dp[N])
