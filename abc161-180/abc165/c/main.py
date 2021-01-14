import math
from functools import reduce
from collections import deque
N,M,Q=map(int,input().split())
a=[None]*Q
b=[None]*Q
c=[None]*Q
d=[None]*Q
for i in range(Q):
	a[i],b[i],c[i],d[i]=map(int,input().split())

ans=0
A=[None]*N
def dfs(start, end, siz, pos):
	if pos == siz:
		global ans
		point=0
		for i in range(Q):
			if A[b[i] - 1] - A[a[i] - 1] == c[i]:
				point += d[i]
		ans=max(ans, point)
		return
	for i in range(start, end):
		A[pos] = i
		dfs(i, end, siz, pos+1)

dfs(1, M+1, N, 0)
print(ans)
