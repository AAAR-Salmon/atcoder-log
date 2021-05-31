N, K = map(int,input().split())
pre = ''
rle = []
for c in input():
	if c != pre:
		rle.append([c, 1])
		pre = c
	else:
		rle[-1][1] += 1

ans = s = 0
l = r = 0
z = 0
for r in range(len(rle)):
	c, rl = rle[r]
	s += rl
	r += 1
	if c == '0':
		z += 1
	while z > K:
		c, rl = rle[l]
		s -= rl
		l += 1
		if c == '0':
			z -= 1
	ans = max(ans, s)
print(ans)
