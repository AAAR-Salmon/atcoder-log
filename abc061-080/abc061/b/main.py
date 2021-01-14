import math
from functools import reduce
from collections import deque
N,M = map(int,input().split())
ans = [0] * N
for i in range(M):
	a,b = map(lambda x:int(x)-1,input().split())
	ans[a] += 1
	ans[b] += 1
print(*ans, sep='\n')
