from sys import setrecursionlimit
setrecursionlimit(1000000)
from itertools import chain

N = int(input())
C = list(chain([0], map(int,input().split())))
edge = [[] for _ in range(N + 1)]
for _ in range(N - 1):
	A,B = map(int,input().split())
	edge[A].append(B)
	edge[B].append(A)

count_colors = [0] * 100001
is_vertex_good = [False] * (N+1)
done = [False] * (N+1)

def dfs(fr):
	if done[fr]:
		return
	done[fr] = True
	for to in edge[fr]:
		color = C[to]
		if count_colors[color] == 0:
			is_vertex_good[to] = True
		count_colors[color] += 1
		dfs(to)
		count_colors[color] -= 1

is_vertex_good[1] = True
count_colors[C[1]] += 1
dfs(1)
print(*(i for i, v in enumerate(is_vertex_good) if v), sep='\n')
