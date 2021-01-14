import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

N,A,B,C = map(int,input().split())
l = [int(input()) for _ in range(N)]

def dfs(i,a,b,c):
	if i == N:
		if a == 0 or b == 0 or c == 0:
			return 100000
		else:
			return abs(a - A) + abs(b - B) + abs(c - C) - 30
	return min(
		dfs(i+1, a, b, c),
		dfs(i+1, a+l[i], b, c) + 10,
		dfs(i+1, a, b+l[i], c) + 10,
		dfs(i+1, a, b, c+l[i]) + 10)

print(dfs(0,0,0,0))
