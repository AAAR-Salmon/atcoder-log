import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

S = {'a': 0, 'b': 0, 'c': 0}
for c in input():
	S[c] += 1
if abs(S['a'] - S['b']) > 1 or abs(S['b'] - S['c']) > 1 or abs(S['c'] - S['a']) > 1:
	print('NO')
else:
	print('YES')
