import math
from functools import reduce
from collections import deque
n = int(input())
left = 0
right = n + 1
while right - left > 1:
	mid = (left + right) // 2
	if mid * (mid + 1) // 2 <= n + 1:
		left = mid
	else:
		right = mid
print(n - right + 2)
