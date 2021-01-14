import math
from functools import reduce
from collections import deque
X=int(input())
for A in range(-118, 120):
	ng=119
	ok=-120
	while ng-ok>1:
		mid=(ok+ng)//2
		if A ** 5 - mid ** 5 >= X:
			ok=mid
		else:
			ng=mid
	if A ** 5 - ok ** 5 == X:
		print(A,ok)
		break
