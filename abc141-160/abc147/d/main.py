import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

MOD = 10**9+7

N = int(input())
A = list(map(int,input().split()))

ans = 0
for i in range(60):
	O = I = 0
	for a in A:
		if a & 1 << i:
			I += 1
		else:
			O += 1
	ans = (ans + I * O * (1 << i)) % MOD
print(ans)
