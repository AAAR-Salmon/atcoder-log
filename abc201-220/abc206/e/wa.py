from operator import mul


L, R = map(int, input().split())

spf = list(range(R + 1))
for i in range(2, R + 1):
	if spf[i] == i:
		for j in range(i, R + 1, i):
			if spf[j] == j:
				spf[j] = i


def popcount(x):
	assert (0 <= x <= 0xFFFFFFFF)
	x = x - (x >> 1 & 0x55555555)
	x = (x & 0x33333333) + (x >> 2 & 0x33333333)
	x = (x + (x >> 4)) & 0x0f0f0f0f
	x = (x + (x >> 8)) & 0x00ff00ff
	x = (x + (x >> 16)) & 0x0000ffff
	return x


ans = 0
for x in range(L, R + 1):
	if spf[x] == x:
		continue
	pf = set()
	x_ = x
	while x_ > 1:
		pf.add(spf[x_])
		x_ //= spf[x_]
	pf = list(pf)
	for gbit in range(1, 1 << len(pf)):
		g = 1
		for i in range(len(pf)):
			if gbit >> i & 1:
				g *= pf[i]
		if x == g:
			continue
		if popcount(gbit) % 2 == 1:
			ans += R // g - (L + g - 1) // g + 1
			if L <= g <= R:
				ans -= 1
		else:
			ans -= R // g - (L + g - 1) // g + 1
			if L <= g <= R:
				ans += 1
print(ans)