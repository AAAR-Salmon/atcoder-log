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

L=[None]*N
def dfs(start, end, siz, pos):
	if pos == siz:
		yield L
		return
	for i in range(start, end):
		L[pos] = i
		for f in dfs(i, end, siz, pos+1):
			yield f

ans=0
gen=dfs(1, M+1, N, 0)
for A in gen:
	point=0
	for i in range(Q):
		if A[b[i] - 1] - A[a[i] - 1] == c[i]:
			point += d[i]
	ans=max(ans, point)
print(ans)
