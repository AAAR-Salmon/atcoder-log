import math
from functools import reduce
from collections import deque
N,X,Y=map(int,input().split())
l = [0] * 2001
for j in range(2,N+1):
	for i in range(1,j):
		l[min(j - i, abs(X - i) + abs(Y - j) + 1)] += 1
for k in range(1,N):
	print(l[k])
