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
ans = 0
for i in range(N-3):
	s = int(S[i:i+3])
	for j in range(i+3,N):
		s = (s * 10 + int(S[j])) % 2019
		if s == 0:
			ans += 1
print(ans)
