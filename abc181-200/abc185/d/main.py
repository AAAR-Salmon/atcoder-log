import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

N,M = map(int,input().split())
A = [0]
A.extend(sorted(map(int,input().split())))
A.append(N+1)
SP = []
for i in range(M+1):
	if A[i+1]-A[i]-1 > 0:
		SP.append(A[i+1]-A[i]-1)
ans = 0
if SP != []:
	k = min(SP)
	for s in SP:
		ans += (s+k-1)//k
print(ans)
