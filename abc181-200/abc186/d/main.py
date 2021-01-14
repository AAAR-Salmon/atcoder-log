import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

N = int(input())
A = list(map(int,input().split()))
A.sort()
ans = 0
dp = [0] * (N+1)
for i in range(0,N):
	dp[i+1] = dp[i] + A[i]
for i in range(1,N):
	ans += A[i] * i - dp[i]
print(ans)
