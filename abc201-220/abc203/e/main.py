from collections import defaultdict

N, M = map(int, input().split())
black = defaultdict(set)
for i in range(M):
	x, y = map(int, input().split())
	black[x].add(y)
dp = set([N])
for i in sorted(black.keys()):
	dpadd = set()
	dprem = set()
	for j in black[i]:
		if j not in dp and (j - 1 in dp or j + 1 in dp):
			dpadd.add(j)
		if j in dp and (j - 1 not in dp and j + 1 not in dp):
			dprem.add(j)
	for j in dpadd:
		dp.add(j)
	for j in dprem:
		dp.remove(j)
print(len(dp))
