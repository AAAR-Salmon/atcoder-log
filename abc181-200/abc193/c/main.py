import sys
sys.setrecursionlimit(1000000)
import math
from math import sin, cos, tan, gcd
from functools import reduce
from collections import deque
from heapq import heapify, heappush, heappop
intm1 = lambda x:int(x)-1

N = int(input())
expressable = set()
for b in range(2, 34):
	a = 2
	while a ** b <= N:
		expressable.add(a ** b)
		a += 1
print(N - len(expressable))
