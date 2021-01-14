import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

N = input()
S = sum(map(int,N))
N = int(N)
print('Yes' if N % S == 0 else 'No')
