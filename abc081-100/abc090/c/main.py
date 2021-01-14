import math
from functools import reduce
from collections import deque
N,M = map(int,input().split())
ans = 0
if N > 2 and M > 2:
	ans += (N-2) * (M-2)
if N == 1 or M == 1:
	if N == 1 and M == 1:
		ans += 1
	else:
		ans += max(N,M)-2
print(ans)
