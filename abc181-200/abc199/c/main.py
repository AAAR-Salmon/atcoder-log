import sys
sys.setrecursionlimit(1000000)
import math
from math import sin, cos, tan, gcd
from functools import reduce
from collections import deque
from itertools import chain, permutations
from heapq import heapify, heappush, heappop

MOD = 1_000_000_007
# MOD = 998_244_353
dpos4 = ((-1, 0), (0, -1), (0, 1), (1, 0))
dpos8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

N = int(input())
S = bytearray(input().encode())
filpped = False
Q = int(input())
for i in range(Q):
	T,A,B = map(int,input().split())
	if T == 1:
		A -= 1
		B -= 1
		if filpped:
			A = (A + N) % (2 * N)
			B = (B + N) % (2 * N)
		S[A], S[B] = S[B], S[A]
	else:
		filpped = not filpped
S1 = str(S[:N].decode())
S2 = str(S[N:].decode())
if filpped:
	S1, S2 = S2, S1
print(S1, S2, sep='')
