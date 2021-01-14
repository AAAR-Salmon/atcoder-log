import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

N,K = map(int,input().split())
A = list(map(int,input().split()))

left = 0
right = max(A)+1
while right - left > 1:
	mid = (left + right) // 2
	X = sum(map(lambda a:(a+mid-1)//mid-1,A))
	if X <= K:
		right = mid
	else:
		left = mid
print(right)
