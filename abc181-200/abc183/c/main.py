import math
from functools import reduce
from collections import deque

N,K=map(int,input().split())
T=[list(map(int,input().split())) for _ in range(N)]

A=[0] * N
done=[False] * N
ans=0
def dfs(pos):
	if pos == N:
		time=0
		for i in range(N):
			time += T[A[i-1]][A[i]]
		if time == K:
			global ans
			ans += 1
		return
	for i in range(1, N):
		if done[i]:
			continue
		done[i] = True
		A[pos] = i
		dfs(pos+1)
		done[i] = False
dfs(1)
print(ans)
