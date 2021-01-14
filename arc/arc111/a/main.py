import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

N,M = map(int,input().split())
print(math.floor(10 ** ((N - math.log10(M)) % math.log10(M))) % M)
