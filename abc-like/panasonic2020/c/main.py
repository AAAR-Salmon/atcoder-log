import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

a,b,c = map(int,input().split())
# c-a-b>2sqrt(ab)
if c-a-b > 0 and 4*a*b < (c-a-b) ** 2:
	print('Yes')
else:
	print('No')
