import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

n,m,d = map(int,input().split())
if d >= n:
    print(0)
elif d == 0:
    print((m - 1) / n)
else:
    print((m - 1) * (n - d) * 2 / n ** 2)
