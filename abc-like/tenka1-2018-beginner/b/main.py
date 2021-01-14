import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

A,B,K = map(int,input().split())
for i in range(K):
	if i % 2 == 0: #takahashi
		if A % 2 == 1:
			A -= 1
		B += A // 2
		A //= 2
	else: # aoki
		if B % 2 == 1:
			B -= 1
		A += B // 2
		B //= 2
print(A,B)
