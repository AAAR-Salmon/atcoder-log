import sys
import math
from math import sin, cos, tan
from math import gcd
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

def test():
	N, S, K = map(int,input().split())
	K %= N
	g = gcd(K, N)
	# ans = min(x; x >= 0 and y >= 0) : S + K * x == N * y
	# 解無し
	if S % g != 0:
		print(-1)
		return
	# とりあえず約分
	S //= g
	K //= g
	N //= g
	# K * x - N * y == 1 の特殊解を求める
	print(f'{K}x-{N}y=1: {exgcd(K,N)}')

def exgcd(a,b):
	if b == 0:
		return (1,0)
	else:
		y,x = exgcd(b, a%b)
		return (x,y-a//b*x)

T = int(input())
for i in range(T):
	test()
