import heapq
INF = 1000000000

N,M = map(int,input().split())
Conj = [[] for _ in range(N+1)]

for i in range(M):
	a,b,c = map(int,input().split())
	Conj[a].append((b,c))

for i in range(1,N+1):
	h = [(0,i)]
	done = [INF] * (N+1)
	while h:
		minpath, node = heapq.heappop(h)
		for next, cost in Conj[node]:
			if minpath + cost < done[next]:
				done[next] = minpath + cost
				heapq.heappush(h, (minpath + cost, next))
	print(-1 if done[i] == INF else done[i])
