import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

N,M = map(int,input().split())
A = sorted(map(int,input().split()))
BC = sorted(
	(list(map(int,input().split())) for _ in range(M)),
	key=lambda x:x[1],
	reverse=True)
i = j = k = 0
while i < N and j < M:
	if A[i] < BC[j][1]:
		A[i] = BC[j][1]
		i += 1
		k += 1
		if k == BC[j][0]:
			j += 1
			k = 0
	else:
		break
print(sum(A))