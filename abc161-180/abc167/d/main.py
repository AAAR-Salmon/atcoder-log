import math
from functools import reduce
from collections import deque
intm1 = lambda x:int(x)-1
N,K = map(int,input().split())
A = list(map(intm1,input().split()))
p = [0] * N
visited = [-1] * N
visited[0] = 0
for i in range(0,N):
	if visited[A[p[i]]] != -1:
		loopstart = visited[A[p[i]]]
		loopend = i+1
		break
	else:
		p[i+1] = A[p[i]]
		visited[p[i+1]] = i+1
if K < loopstart:
	print(p[K] + 1)
else:
	print(p[loopstart + (K - loopstart) % (loopend - loopstart)] + 1)
