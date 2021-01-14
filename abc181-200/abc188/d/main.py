import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

N,C = map(int,input().split())
ev = [None] * N*2
for i in range(N):
	a,b,c = map(int,input().split())
	ev[2*i] = (a,c)
	ev[2*i+1] = (b+1,-c)

ev.sort(key=lambda x:x[0])
pt = ev[0][0]
nc = 0
ans = 0
for (k, c) in ev:
	if pt != k:
		ans += (k - pt) * min(nc,C)
		pt = k
	nc += c
print(ans)
