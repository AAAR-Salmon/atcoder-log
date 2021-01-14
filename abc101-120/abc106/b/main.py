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
for i in range(1, N+1, 2):
	j = 1
	cnt = 0
	while j ** 2 < i:
		if i % j == 0:
			cnt += 2
		j += 1
	if j ** 2 == i:
		cnt += 1
	if cnt == 8:
		ans += 1
print(ans)
