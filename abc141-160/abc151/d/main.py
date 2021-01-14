import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

INF = 400
H,W = map(int,input().split())
S = [input() for _ in range(H)]
dp = [[INF] * (H*W) for _ in range(H*W)]

for i in range(H*W):
	dp[i][i] = 0

for i in range(H):
	for j in range(W-1):
		if S[i][j] == S[i][j+1] == '.':
			dp[i*W+j][i*W+(j+1)] = 1
			dp[i*W+(j+1)][i*W+j] = 1

for i in range(H-1):
	for j in range(W):
		if S[i][j] == S[i+1][j] == '.':
			dp[i*W+j][(i+1)*W+j] = 1
			dp[(i+1)*W+j][i*W+j] = 1

for k in range(H*W):
	for i in range(H*W):
		for j in range(H*W):
			if dp[i][j] > dp[i][k] + dp[k][j]:
				dp[i][j] = dp[i][k] + dp[k][j]
ans = 0
for i in range(H*W):
	for j in range(H*W):
		if ans < dp[i][j] < INF:
			ans = dp[i][j]
print(ans)
