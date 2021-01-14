import math
from functools import reduce
from collections import deque
N=int(input())
for i in range(1, 10):
	if 111 * i >= N:
		ans = 111 * i
		break
print(ans)
