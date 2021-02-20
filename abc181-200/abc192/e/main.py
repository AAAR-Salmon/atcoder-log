from heapq import heappop, heappush

N,M,X,Y = map(int,input().split())
adj = [[] for _ in range(N+1)]
for i in range(M):
	A,B,T,K = map(int,input().split())
	adj[A].append((B, T, K))
	adj[B].append((A, T, K))

INF = 10**15
dp = [INF] * (N+1)
dp[X] = 0
hq = [X]
while hq:
	cur = heappop(hq)
	cur_time = dp[cur]
	for next, T, K in adj[cur]:
		ariv_time = (cur_time + K - 1) // K * K + T
		if ariv_time < dp[next]:
			dp[next] = ariv_time
			heappush(hq, next)
print(dp[Y] if dp[Y] < INF else -1)
