import math
from functools import reduce
from collections import deque
K = int(input())
q = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
for i in range(K):
	X = q.popleft()
	d = X % 10
	if d > 0:
		q.append(10*X + d-1)
	q.append(10*X + d)
	if d < 9:
		q.append(10*X + d+1)
print(X)
