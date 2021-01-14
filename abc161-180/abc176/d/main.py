import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

H,W = map(int,input().split())
Ch,Cw = map(intm1,input().split())
Dh,Dw = map(intm1,input().split())
S = [input() for _ in range(H)]

dp = [[None] * W for _ in range(H)]
dp[Ch][Cw] = 0
q = deque([(Ch,Cw)])
while q:
	x,y = q.popleft()
	if (x,y) == (Dh,Dw):
		break
	for dx,dy in [(-1,0),(0,-1),(0,1),(1,0)]:
		if x+dx < 0 or H <= x+dx or y+dy < 0 or W <= y+dy:
			continue
		if S[x+dx][y+dy] == '#':
			continue
		if dp[x+dx][y+dy] == None or dp[x][y] < dp[x+dx][y+dy]:
			dp[x+dx][y+dy] = dp[x][y]
			q.appendleft((x+dx,y+dy))

	for dx,dy in [(-2,-2),(-2,-1),(-2,0),(-2,1),(-2,2),
	              (-1,-2),(-1,-1),       (-1,1),(-1,2),
	              ( 0,-2),                       (0,2),
	              ( 1,-2), (1,-1),        (1,1), (1,2),
	              ( 2,-2), (2,-1), (2,0), (2,1), (2,2)]:
		if x+dx < 0 or H <= x+dx or y+dy < 0 or W <= y+dy:
			continue
		if S[x+dx][y+dy] == '#':
			continue
		if dp[x+dx][y+dy] == None or dp[x][y]+1 < dp[x+dx][y+dy]:
			dp[x+dx][y+dy] = dp[x][y]+1
			q.append((x+dx,y+dy))

print(-1 if dp[Dh][Dw] == None else dp[Dh][Dw])
