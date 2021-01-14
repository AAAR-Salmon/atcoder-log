import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

N = int(input())
A,B = [None] * N, [None] * N
for i in range(N):
	A[i],B[i] = map(int,input().split())
p = sorted(((i, B[i]) for i in range(N)), key=lambda x:x[1])
t = 0
ans = 'Yes'
for i in range(N):
	t += A[p[i][0]]
	if t > B[p[i][0]]:
		ans = 'No'
		break
print(ans)