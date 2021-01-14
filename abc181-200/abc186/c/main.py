import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

N = int(input())
ans = 0
s = ''
for i in range(1,N+1):
	if '7' in str(i) or '7' in oct(i):
		pass
	else:
		ans += 1
print(ans)
