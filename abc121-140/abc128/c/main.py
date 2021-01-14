import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

N,M = map(int,input().split())
k = [None] * M
s = [None] * M
for i in range(M):
	q = input().split()
	k[i] = int(q[0])
	s[i] = list(map(intm1,q[1:]))
p = list(map(int,input().split()))
ans = 0
for sw in range(1 << N):
	ok = all(reduce(lambda x,y:x^y, map(lambda x:(sw & 1 << x) >> x, s[i])) == p[i] for i in range(M))
	if ok:
		ans += 1
print(ans)
