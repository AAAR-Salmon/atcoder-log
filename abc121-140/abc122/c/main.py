import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

N,Q = map(int,input().split())
S = input()
countACl = [0] * (N+1)
countACr = [0] * (N+1)
isLastCharA = False
for i in range(N):
	if isLastCharA:
		if S[i] == 'C':
			countACl[i] = 1
			countACr[i+1] = 1
	isLastCharA = S[i] == 'A'
for i in range(1,N+1):
	countACl[i] += countACl[i-1]
	countACr[i] += countACr[i-1]
#print(countAC)
for _ in range(Q):
	l,r = map(int,input().split())
	print(countACr[r]-countACl[l-1])
