import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

N,M = map(int,input().split())
AB = [list(map(int,input().split())) for _ in range(M)]
K = int(input())
CD = [list(map(int, input().split())) for _ in range(K)]
ans = 0
for bit in range(1 << K):
	# bitが0 => Cに置く
	put = set()
	for i in range(K):
		if bit & 1 << i:
			put.add(CD[i][1])
		else:
			put.add(CD[i][0])
	count = 0
	for i in range(M):
		if AB[i][0] in put and AB[i][1] in put:
			count += 1
	if count > ans:
		ans = count
print(ans)
