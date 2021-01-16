import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1
MOD = 998244353

H,W,K = map(int,input().split())
c = [['.'] * (W+1) for _ in range(H+1)]

for i in range(K):
	h,w,ch = input().split()
	h,w = map(int,(h,w))
	c[h][w] = ch

dp = [[0] * (W+1) for _ in range(H+1)]
# 始端処理を楽にするためにdp[1][1] = 1になるよう調節
for j in range(W+1):
	c[0][j] = 'R'
for i in range(1,H+1):
	c[i][0] = 'D'
dp[1][1] = 1

for i in range(1,H+1):
	for j in range(1,W+1):
		if c[i-1][j] == 'D' or c[i-1][j] == 'X':
			dp[i][j] += dp[i-1][j]
		elif c[i-1][j] == '.':
			dp[i][j] += dp[i-1][j] * 2
		if c[i][j-1] == 'R' or c[i][j-1] == 'X':
			dp[i][j] += dp[i][j-1]
		elif c[i][j-1] == '.':
			dp[i][j] += dp[i][j-1] * 2
		dp[i][j] %= MOD
print(dp[H][W])
