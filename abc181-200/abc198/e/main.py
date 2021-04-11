from collections import deque
from itertools import chain
from copy import copy

N = int(input())
C = list(chain([0], map(int,input().split())))
edge = [[] for _ in range(N + 1)]
for _ in range(N - 1):
	A,B = map(int,input().split())
	edge[A].append(B)
	edge[B].append(A)

good = [False] * (N + 1)
good[1] = True
path_from_1 = set([C[1]])
s = deque([1])
sorted_nodes = []

while s:
	n = s.pop()
	sorted_nodes.append(n)
	for c in edge[n]:
		s.append(c)

while s:
	n = s.pop()
	for x in edge[n]:
		if done[x] != None:
			continue
		if not C[x] in path_from_1:
			path_from_1.add(C[x])
			good[x] = True
		s.append(x)
print(*(i for i in range(N + 1) if good[i]), sep='\n')
