N, H = map(int, input().split())
A, B, C, D, E = map(int, input().split())

# H + B * x + D * y - E * (N - x - y) > 0
# (D + E) * y > E * N - H - (B + E) * x
ans = 1 << 60
for x in range(N + 1):
	l, r = -1, N - x + 1
	while r - l > 1:
		m = (l + r) // 2
		if H + B * x + D * m - E * (N - x - m) > 0:
			r = m
		else:
			l = m
	if x + r > N:
		continue
	else:
		y = r
	ans = min(ans, A * x + C * y)

print(ans)
