B,C = map(int,input().split())
a = -B - max(C - 1, 0) // 2
b = -B + max(C - 1, 0) // 2
c = B - C // 2
d = B + max(C - 2, 0) // 2
if B <= 0:
	a,b,c,d = c,d,a,b
if c > b:
	print(d - c + 1 + b - a + 1)
else:
	print(d - a + 1)
