from collections import deque

N, M = map(int, input().split())
edges = [[] for _ in range(N + 1)]
for _ in range(M):
	A, B = map(int, input().split())
	edges[A].append(B)

ans = 0
for s in range(1, N + 1):
	done = [False] * (N + 1)
	done[s] = True
	ans += 1
	st = deque([s])
	while st:
		fr = st.pop()
		for to in edges[fr]:
			if done[to]:
				continue
			done[to] = True
			st.append(to)
			ans += 1

print(ans)
