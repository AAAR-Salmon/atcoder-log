import itertools

N = int(input())
p = [tuple(map(int,input().split())) for _ in range(N)]

for cx, cy in itertools.product(range(101), repeat=2):
	for x, y, h in p:
		if h != 0:
			H = h + abs(x - cx) + abs(y - cy)
			break
	satisfiable = True
	for x, y, h in p:
		if h != max(H - abs(x - cx) - abs(y - cy), 0):
			satisfiable = False
			break
	if not satisfiable:
		continue
	print(cx, cy, H)
	break
