from functools import reduce
from itertools import combinations_with_replacement
import operator
from sys import stderr

N = int(input())
status = [tuple(map(int,input().split())) for _ in range(N)]

l = 0
r = 1_000_000_001
while r - l > 1:
	m = (l + r) // 2
	geq = [False] * (1 << 5)
	for s in status:
		b = 0
		for j in range(5):
			b |= (s[j] >= m) << j
		geq[b] = True
	geq = [i for i in range(1 << 5) if geq[i]]
	if any(reduce(operator.or_, c) == 0b11111 for c in combinations_with_replacement(geq, 3)):
		l = m
	else:
		r = m
print(l)
