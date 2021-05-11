INF = 1_000_000_000

N = int(input())
cities = [tuple(map(int,input().split())) for _ in range(N)]

cost = [[(
	abs(cities[to][0] - cities[fr][0]) +
	abs(cities[to][1] - cities[fr][1]) +
	max(cities[to][2] - cities[fr][2], 0)
) for to in range(N)] for fr in range(N)]

dp = [[INF] * N for _ in range(1 << N)]
dp[1][0] = 0
for done in range(1 << N):
	for fr in range(N):
		if done >> fr & 1:
			for to in range(N):
				dp[done | 1 << to][to] = min(dp[done | 1 << to][to], dp[done][fr] + cost[fr][to])

print(dp[-1][0])
