import math
from functools import reduce
from collections import deque

N,M,X,Y = map(int,input().split())
x = list(map(int,input().split()))
y = list(map(int,input().split()))

ans = 'War'
for Z in range(X+1,Y+1):
	if max(x) < Z <=min(y):
		ans = 'No War'
		break
print(ans)
