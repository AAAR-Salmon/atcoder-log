import math
from functools import reduce
from collections import deque
N = int(input())
if N == 0:
	print(0)
	exit(0)
F = {}
i = 2
while i * i <= N:
	if N % i == 0:
		F[i] = 0
		while N % i == 0:
			F[i] += 1
			N //= i
	i += 1
if N != 1:
	F[N] = 1
ans = 0
for v in F.values():
	left = 0
	right = v + 1
	while right - left > 1:
		mid = (left + right) // 2
		if mid * (mid + 1) // 2 <= v:
			left = mid
		else:
			right = mid
	ans += left
print(ans)
