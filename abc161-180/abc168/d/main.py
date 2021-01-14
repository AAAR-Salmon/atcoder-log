import math
from functools import reduce
from collections import deque
intm1 = lambda x:int(x)-1
N,M = map(int,input().split())
conj = [[] for _ in range(N)]
for _ in range(M):
	a,b = map(intm1,input().split())
	conj[a].append(b)
	conj[b].append(a)
q = deque([(-1,0,0)])
ans = [(-1,100005) for _ in range(N)]
while q:
	prev,pos,cost = q.popleft()
	if cost < ans[pos][1]:
		ans[pos] = (prev,cost)
		for next in conj[pos]:
			q.append((pos,next,cost+1))
print('Yes')
print(*map(lambda x:x[0]+1,ans[1:]), sep='\n')
