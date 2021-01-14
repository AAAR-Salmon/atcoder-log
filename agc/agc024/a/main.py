import math
from functools import reduce
from collections import deque
A,B,C,K = map(int,input().split())
# a[i] = (2**i * (A+B+C) - (-1)**i * (-2*A+B+C)) // 3
# b[i] = (2**i * (A+B+C) - (-1)**i * (A-2*B+C)) // 3
# a[K] - b[K]
if K % 2 == 0:
	print(A-B)
else:
	print(B-A)
