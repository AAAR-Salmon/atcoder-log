import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

N = int(input())
A = list(map(int,input().split()))
f1 = 1
f1v = 0
f2 = 2 ** (N - 1) + 1
f2v = 0
for i in range(0, 2 ** (N - 1)):
	if A[i] > f1v:
		f1v = A[i]
		f1 = i
for i in range(2 ** (N - 1), 2 ** N):
	if A[i] > f2v:
		f2v = A[i]
		f2 = i
ans = f1 if f1v < f2v else f2
print(ans + 1)
