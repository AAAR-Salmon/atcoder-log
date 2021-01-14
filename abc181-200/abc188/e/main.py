import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

N,M = map(int,input().split())
A = list(map(int,input().split()))
dp = [0] * N
parent = [[] for _ in range(N)]
child = [[] for _ in range(N)]
for i in range(M):
	X,Y = map(intm1,input().split())
	parent[Y].append(X)
	child[X].append(Y)

leaves = [i for i in range(N) if not child[i]]
q = deque(leaves)
while q:
	n = q.popleft()
	P = parent[n]
	if not P:
		continue
	for p in P:
		if max(dp[n], A[n]) > dp[p]:
			dp[p] = max(dp[n], A[n])
			q.append(p)

ans = max(dp[i] - A[i] for i in range(N) if child[i])
print(ans)
