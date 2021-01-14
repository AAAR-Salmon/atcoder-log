import math
from functools import reduce
from collections import deque
N,x = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
i = 0
while i < N:
	if i == N-1:
		if x == a[i]:
			x -= a[i]
			i += 1
		else:
			break
	elif x >= a[i]:
		x -= a[i]
		i += 1
	else:
		break
print(i)
