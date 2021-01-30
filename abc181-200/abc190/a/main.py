import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

A,B,C = map(int,input().split())
if A > B or A == B and C == 1:
	print('Takahashi')
else:
	print('Aoki')
