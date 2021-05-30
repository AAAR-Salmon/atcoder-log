import sys
sys.setrecursionlimit(1000000)
import math
from math import sin, cos, tan, gcd
from functools import reduce
from collections import deque
from itertools import chain, permutations
from heapq import heapify, heappush, heappop

MOD = 1_000_000_007
# MOD = 998_244_353
dpos4 = ((-1, 0), (0, -1), (0, 1), (1, 0))
dpos8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

a,b,c = map(int,input().split())
if a == b:
	print(c)
elif b == c:
	print(a)
elif c == a:
	print(b)
else:
	print(0)
