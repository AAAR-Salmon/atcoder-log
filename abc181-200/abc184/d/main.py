import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)

A,B,C = map(int,input().split())
dp = [[[0]*101 for _ in range(101)] for _ in range(101)]
dp[A][B][C] = 1
for a in range(A,100):
	for b in range(B,100):
		for c in range(C,100):
			dp[a+1][b][c] += dp[a][b][c] * a / (a+b+c)
			dp[a][b+1][c] += dp[a][b][c] * b / (a+b+c)
			dp[a][b][c+1] += dp[a][b][c] * c / (a+b+c)
e = 0
for b in range(B,100):
	for c in range(C,100):
		e += ((100-A) + (b-B) + (c-C)) * dp[100][b][c]

for a in range(A,100):
	for c in range(C,100):
		e += ((a-A) + (100-B) + (c-C)) * dp[a][100][c]

for a in range(A,100):
	for b in range(B,100):
		e += ((a-A) + (b-B) + (100-C)) * dp[a][b][100]

print(e)
