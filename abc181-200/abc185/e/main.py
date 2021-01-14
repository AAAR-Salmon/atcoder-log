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
B = list(map(int,input().split()))

dp = [[0] * (M+1) for _ in range(N+1)]
for i in range(N+1):
	for j in range(M+1):
		if i == 0 or j == 0:
			dp[i][j] = i+j
		else:
			dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+(1 if A[i-1] != B[j-1] else 0))
print(dp[N][M])
