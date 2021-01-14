import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

X,Y = map(int,input().split())
if Y <= X:
	print(X - Y)
	exit(0)
