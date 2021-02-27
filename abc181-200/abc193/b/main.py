import sys
sys.setrecursionlimit(1000000)
import math
from math import sin, cos, tan, gcd
from functools import reduce
from collections import deque
from heapq import heapify, heappush, heappop
intm1 = lambda x:int(x)-1

N = int(input())
Y = [tuple(map(int,input().split())) for _ in range(N)]
Y.sort(key=lambda x:x[1])
ans = -1
for A,P,X in Y:
	if X - A > 0:
		ans = P
		break
print(ans)
