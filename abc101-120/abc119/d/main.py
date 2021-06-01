from itertools import chain
from sys import stdin

INF = 1 << 60
Input = stdin.readlines()

A, B, Q = map(int, Input[0].split())
s = sorted(chain(map(int, Input[1:1 + A]), [-INF, INF]))
t = sorted(chain(map(int, Input[1 + A:1 + A + B]), [-INF, INF]))

for i in range(Q):
	x = int(Input[1 + A + B + i])

	la, ra = -1, A + 2
	while ra - la > 1:
		m = (la + ra) // 2
		if s[m] > x:
			ra = m
		else:
			la = m

	lb, rb = -1, B + 2
	while rb - lb > 1:
		m = (lb + rb) // 2
		if t[m] > x:
			rb = m
		else:
			lb = m

	ls = s[la]
	rs = s[ra]
	lt = t[lb]
	rt = t[rb]
	print(
	    min(x - min(ls, lt),
	        max(rs, rt) - x,
	        min(x - ls, rt - x) + rt - ls,
	        min(rs - x, x - lt) + rs - lt))
