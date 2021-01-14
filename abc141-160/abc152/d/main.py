import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

N = int(input())
dp = [[0] * 9 for _ in range(9)]
for i in range(1,N+1):
	s = str(i)
	a,b = int(s[0]),int(s[-1])
	if a == 0 or b == 0:
		continue
	dp[a-1][b-1] += 1
print(sum(dp[i][j] * dp[j][i] for i in range(9) for j in range(9)))
