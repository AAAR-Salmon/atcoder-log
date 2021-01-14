import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

MOD = 10**9+7
N,M = map(int,input().split())
dp = [0] * (N+1)
dp[0] = 1
for _ in range(M):
	dp[int(input())] = -1

for i in range(1,N+1):
	if dp[i] != -1:
		if dp[i-1] != -1:
			dp[i] += dp[i-1]
		if i-2 >= 0 and dp[i-2] != -1:
			dp[i] += dp[i-2]
		dp[i] %= MOD
print(dp[N])
