import math


R,X,Y = map(int,input().split())
ans2 = (X ** 2 + Y ** 2) / R ** 2
l = -1
r = 1_000_000
while r - l > 1:
	m = (l + r) // 2
	if m ** 2 >= ans2:
		r = m
	else:
		l = m
print(math.ceil(math.sqrt(ans2)))
