from itertools import permutations

N,M = map(int,input().split())
adj = [set() for _ in range(N+1)]
ans = 0

for _ in range(M):
	a,b = map(int,input().split())
	adj[a].add(b)
	adj[b].add(a)

for p in permutations([i+1 for i in range(N)]):
	if p[0] != 1:
		break
	ans += all(p[i+1] in adj[p[i]] for i in range(N-1))
print(ans)
