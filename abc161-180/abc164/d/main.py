import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

S = input()
N = len(S)
# dp[i] = int(S[i:]) % 2019
dp = [0] * N
dp[-1] = int(S[-1])
# remset[i] = dp.count(i) + (1 if i == 0 else 0)
remset = [0] * (2019+1)
remset[0] = 1
remset[dp[-1]] += 1
for i in range(1,N):
	dp[-(i+1)] = (dp[-i] + int(S[-(i+1)]) * pow(10,i,2019)) % 2019
	remset[dp[-(i+1)]] += 1
print(sum(map(lambda x:x*(x-1)//2,remset)))
