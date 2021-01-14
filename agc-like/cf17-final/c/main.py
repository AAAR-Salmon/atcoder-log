import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

N = int(input())
D = [0] * 13
for d in map(int,input().split()):
	D[d] += 1
if D[0] >= 1 or any(D[i] >= 3 for i in range(1,12)) or D[12] >= 2:
	print(0)
	exit(0)
Dc = [0] * 24
Dc[0] = 1
Dc[12] = D[12]
D1 = []
for i in range(1,12):
	if D[i] == 2:
		Dc[i] = Dc[24-i] = 1
	else:
		D1.append(i)
s = 1
for i in range(1 << len(D1)):
	Dcc = Dc[:]
	for j in range(len(D1)):
		if i & 1 << j:
			Dcc[D1[j]] = 1
		else:
			Dcc[24 - D1[j]] = 1
	t = 24
	if Dcc[23] == 1:
		continue
	p = 0
	for i in range(1,24):
		if Dcc[i] == 1:
			if i - p < t:
				t = i - p
			p = i
	if s < t:
		s = t
print(s)
