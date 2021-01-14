import math
from functools import reduce
from collections import deque
N = int(input())
W = [None] * N
W[0] = input()
i = 1
ans = 'Yes'
while i < N:
	w = input()
	if W[i-1][-1] != w[0] or w in W:
		ans = 'No'
		break
	W[i] = w
	i += 1
print(ans)
