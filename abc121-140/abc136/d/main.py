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
moveto = [None] * N
i = 0
while i < N:
	if S[i] == 'L':
		l = i
		r = i - 1
		while i < N and S[i] == 'L':
			moveto[i] = l - (i - l & 1)
			i += 1
		while r >= 0 and S[r] == 'R':
			moveto[r] = l - (l - r & 1)
			r -= 1
	i += 1
ans = [0] * N
for i in moveto:
	ans[i] += 1
print(*ans)
