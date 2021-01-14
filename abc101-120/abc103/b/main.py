import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

S = input()
N = len(S)
SS = S * 2
T = input()
ans = 'No'
for i in range(N):
	if SS[i:i+N] == T:
		ans = 'Yes'
		break
print(ans)
