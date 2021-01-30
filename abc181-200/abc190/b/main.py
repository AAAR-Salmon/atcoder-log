import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

N,S,D = map(int,input().split())
XY = [list(map(int,input().split())) for _ in range(N)]
print('Yes' if any((XY[i][0] < S and XY[i][1] > D) for i in range(N)) else 'No')

