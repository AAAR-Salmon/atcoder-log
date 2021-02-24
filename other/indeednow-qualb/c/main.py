from heapq import heappush, heappop

N = int(input())
adj = [set() for _ in range(N + 1)]
picked = [False] * (N + 1)
ans = []

for _ in range(N - 1):
	a, b = map(int,input().split())
	adj[a].add(b)
	adj[b].add(a)

hq = [1]
picked[1] = True
while hq:
	cur = heappop(hq)
	ans.append(cur)
	for next in adj[cur]:
		if picked[next]:
			continue
		picked[next] = True
		heappush(hq, next)

print(*ans)
