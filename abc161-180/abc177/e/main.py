from math import gcd
from functools import reduce

N = int(input())
A = list(map(int,input().split()))
M = max(A)

spf = list(range(M + 1))
for i in range(2, M + 1):
	if spf[i] != i:
		continue
	for j in range(i * 2, M + 1, i):
		if spf[j] == j:
			spf[j] = i

ispairwise = True
appeared = [False] * (M + 1)
for a in A:
	s = set()
	while a > 1:
		p = spf[a]
		if appeared[p]:
			ispairwise = False
			break
		s.add(p)
		a //= p
	if not ispairwise:
		break
	for p in s:
		appeared[p] = True

if ispairwise:
	print('pairwise coprime')
	exit(0)

if reduce(gcd, A) == 1:
	print('setwise coprime')
else:
	print('not coprime')
