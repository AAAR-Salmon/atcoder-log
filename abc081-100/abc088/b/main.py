import math
from functools import reduce
from collections import deque
N = int(input())
a = list(map(int,input().split()))
A = B = 0
a.sort(reverse=True)
for i in range(0,N,2):
	A += a[i]
for i in range(1,N,2):
	B += a[i]
print(A-B)
