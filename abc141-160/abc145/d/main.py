import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

MOD = 10**9+7
X,Y = map(int,input().split())
# 斜交座標系 <(1,2),(2,1)> として考えると、
# (X,Y)=m(1,2)+n(2,1) の解
# (m,n)=(1/3)(-X+2Y,2X-Y) について考えればよい
m=-X+2*Y
n=2*X-Y
if (m%3, n%3) == (0,0) and m >= 0 and n >= 0:
	m //= 3
	n //= 3
	perm = lambda n,r:reduce(lambda x,y:x*y%MOD,range(n-r+1,n+1),1)
	if m > n:
		m,n = n,m
	# P(m+n,m)/m!
	ans = perm(m+n,m) * pow(perm(m,m),-1,MOD) % MOD
	print(ans)
else:
	print(0)
