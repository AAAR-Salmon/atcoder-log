import sys
sys.setrecursionlimit(1000000)
import math
from math import sin, cos, tan, gcd
from functools import reduce
from collections import deque
from heapq import heapify, heappush, heappop
intm1 = lambda x:int(x)-1

A,B = map(int,input().split())
# B = A - A * X / 100
# X = (A - B) / A * 100
print((A - B) / A * 100)
