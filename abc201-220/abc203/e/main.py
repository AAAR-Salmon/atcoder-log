from collections import defaultdict
from sys import stderr

N, M = map(int, input().split())
black = defaultdict(set)
for i in range(M):
	x, y = map(int, input().split())
	black[x].add(y)
dp = set([N])
for i in sorted(black.keys()):
	dp2 = set()
	bk = black[i]
	for j in dp:
		if j not in bk:
			dp2.add(j)
		if j + 1 in bk:
			dp2.add(j + 1)
		if j - 1 in bk:
			dp2.add(j - 1)
	dp = dp2
print(len(dp2))
