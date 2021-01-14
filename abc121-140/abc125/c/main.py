import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

def gcd(a,b):
	if b == 0:
		return a
	elif a % b == 0:
		return b
	else:
		return gcd(b,a%b)

N = int(input())
A = list(map(int,input().split()))
L = [0] * N
R = [0] * N
for i in range(1,N):
	L[i] = gcd(L[i-1], A[i-1])
for i in range(N-2,-1,-1):
	R[i] = gcd(R[i+1], A[i+1])
print(max(gcd(L[i], R[i]) for i in range(N)))
