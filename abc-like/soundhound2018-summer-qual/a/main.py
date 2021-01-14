import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

a,b = map(int,input().split())
if a + b == 15:
    print('+')
elif a * b == 15:
    print('*')
else:
    print('x')
