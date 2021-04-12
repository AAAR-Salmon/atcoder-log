R,X,Y = map(int,input().split())
if X ** 2 + Y ** 2 < R ** 2:
	print(2)
	exit(0)
ans2 = (X ** 2 + Y ** 2 + R ** 2 - 1) // R ** 2
l = -1
r = 1_000_000
while r - l > 1:
	m = (l + r) // 2
	if m ** 2 >= ans2:
		r = m
	else:
		l = m
print(r)
