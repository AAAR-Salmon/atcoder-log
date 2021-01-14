import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

S = input()
ans = 0
for c in S:
	if c == '1':
		ans += 1
print(ans)
