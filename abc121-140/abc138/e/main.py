s = input()
N = len(s)
s = map(lambda x: x - 97, s.encode())
t = map(lambda x: x - 97, input().encode())

invs = [[] for _ in range(26)]
for i, c in enumerate(s):
	invs[c].append(i)
ans = 0
p = -1
for c in t:
	invsc = invs[c]
	l, r = -1, len(invsc)
	while r - l > 1:
		m = (l + r) // 2
		if invsc[m] > p:
			r = m
		else:
			l = m
	if r != len(invsc):
		p = invsc[r]
		continue
	ans += N
	p = -1
	l, r = -1, len(invsc)
	while r - l > 1:
		m = (l + r) // 2
		if invsc[m] > p:
			r = m
		else:
			l = m
	if r != len(invsc):
		p = invsc[r]
		continue
	print(-1)
	exit(0)

print(ans + p + 1)
