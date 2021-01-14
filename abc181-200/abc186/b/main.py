import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

H,W = map(int,input().split())
A = [None] * H
m = 101
for i in range(H):
	a = list(map(int,input().split()))
	m = min(m, min(a))
	A[i] = a[:]
ans = -m * H * W
for i in range(H):
	ans += sum(A[i])
print(ans)
