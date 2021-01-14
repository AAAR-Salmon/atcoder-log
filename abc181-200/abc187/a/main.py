import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

A,B = input().split()
SA,SB = map(lambda x:sum(map(int, x)), [A,B])
print(max(SA,SB))