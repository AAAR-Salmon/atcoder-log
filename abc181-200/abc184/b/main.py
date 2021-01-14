import math
from functools import reduce
from collections import deque
N,X=map(int,input().split())
S=input()
for c in S:
	if c == 'o':
		X += 1
	elif c == 'x' and X > 0:
		X -= 1
print(X)
