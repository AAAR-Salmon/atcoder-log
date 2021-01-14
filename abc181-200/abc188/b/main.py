import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
naiseki = 0
for i in range(N):
	naiseki += A[i] * B[i]
print('Yes' if naiseki == 0 else 'No')
