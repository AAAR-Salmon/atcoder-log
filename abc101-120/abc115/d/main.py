import math
from functools import reduce
from collections import deque

N,X=map(int,input().split())
Burger=[1]*51
Patty=[1]*51

def ans(N, X):
	if X == 0:
		return 0
	elif N == 0:
		return 1
	elif X <= Burger[N-1] + 1:
		return ans(N-1, X-1)
	else:
		return Patty[N-1] + 1 + ans(N-1, X-Burger[N-1]-2)

for i in range(N):
	Burger[i+1] = Burger[i] * 2 + 3
	Patty[i+1] = Patty[i] * 2 + 1
print(ans(N,X))
