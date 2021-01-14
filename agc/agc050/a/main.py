import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

N = int(input())
for i in range(N):
	print((i*2+1)%N+1, (i*2+2)%N+1)
