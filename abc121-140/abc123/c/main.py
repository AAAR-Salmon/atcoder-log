import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

N = int(input())
A = [int(input()) for _ in range(5)]
bn = min(A)
print((N + bn - 1) // bn + 4)
