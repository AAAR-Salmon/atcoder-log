import math
from functools import reduce
from collections import deque
N = int(input())
A = list(map(int,input().split()))
ans = 0
end = False
while True:
	for i in range(N):
		if A[i] % 2 != 0:
			end = True
			break
		A[i] = A[i] // 2
	if end:
		break
	ans += 1
print(ans)
