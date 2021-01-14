import math
from functools import reduce
from collections import deque
A,B = map(int,input().split())
g = math.gcd(A,B)
P = {}
i = 2
while i ** 2 <= g:
	if g % i == 0:
		P[i] = 0
		while g % i == 0:
			P[i] += 1
			g //= i
	i += 1
if g != 1:
	P[g] = 1
print(len(P) + 1)
