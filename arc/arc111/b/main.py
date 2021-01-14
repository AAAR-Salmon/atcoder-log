import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

N = int(input())
a = [None] * N
b = [None] * N
for i in range(N):
	a[i], b[i] = map(int,input().split())

