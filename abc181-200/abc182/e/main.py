import sys
sys.setrecursionlimit(1000000)
from functools import reduce
from collections import deque
import heapq
intm1 = lambda x:int(x)-1

H,W,N,M = map(int,input().split())
A = [None] * N
B = [None] * N
C = [None] * M
D = [None] * M
for i in range(N):
	A[i],B[i] = map(intm1,input().split())
for i in range(M):
	C[i],D[i] = map(intm1,input().split())
