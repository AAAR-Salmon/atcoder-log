import math
from functools import reduce
from collections import deque
N,T = map(int,input().split())
path = [[None,None]] * N
for i in range(N):
	path[i] = list(map(int,input().split()))
path.sort(key=lambda x:x[1])
ok=-1
ng=N
while ng - ok > 1:
	mid = (ok+ng)//2
	if path[mid][1] <= T:
		ok = mid
	else:
		ng = mid
if ok==-1:
	print('TLE')
else:
	print(min(path[:ok+1], key=lambda x:x[0])[0])
