import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

x,y,z = map(int,input().split())
n = z
for i in range(17*107):
	if n % 17 == x and n % 107 == y:
		print(n)
		exit(0)
	n += 1000000007
print(n)