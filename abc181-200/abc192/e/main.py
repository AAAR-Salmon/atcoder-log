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
hq = [(0, X)]
while hq:
	cur_time, cur = heappop(hq)
	if dp[cur] < cur_time:
		continue
	for next, T, K in adj[cur]:
		ariv_time = (cur_time + K - 1) // K * K + T
		if ariv_time < dp[next]:
			dp[next] = ariv_time
			heappush(hq, (ariv_time, next))
print(dp[Y] if dp[Y] < INF else -1)
