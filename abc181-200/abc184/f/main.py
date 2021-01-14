import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

N,T = map(int,input().split())
A = list(map(int,input().split()))
B = A[:N//2]
C = A[N//2:]
