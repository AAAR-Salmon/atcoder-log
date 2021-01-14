import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

N = int(input())
A = list(map(int,input().split()))

# j - i == A[i] + A[j]
# <==> i + A[i] == j - A[j]
B = [i + A[i] for i in range(N)]
C = [i - A[i] for i in range(N)]
B.sort()
C.sort()
ans = 0
i = j = 0
while i < N and j < N:
	if B[i] == C[j]:
		v = B[i]
		B_count_v = C_count_v = 0
		while i < N and B[i] == v:
			B_count_v += 1
			i += 1
		while j < N and C[j] == v:
			C_count_v += 1
			j += 1
		ans += B_count_v * C_count_v
	elif B[i] < C[j]:
		i += 1
	else:
		j += 1
print(ans)
