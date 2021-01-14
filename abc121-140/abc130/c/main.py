import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

W,H,x,y = map(int,input().split())
print(W*H/2, 1 if (x*2,y*2) == (W,H) else 0)
