import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

N,M = map(int,input().split())
A = list(map(lambda x:int(x)//2, input().split()))
X = 1
for a in A:
	X = X * a // math.gcd(X, a)
	if X > M:
		print(0)
		exit(0)
print(M // X - M // (2 * X))
