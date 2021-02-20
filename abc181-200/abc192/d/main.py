X = input()
L = len(X)
X_list = list(map(int, reversed(X)))
M = int(input())
d = max(X_list)

if L == 1:
	print(1 if int(X) <= M else 0)
	exit(0)
# L >= 2
l = d
r = M + 1
while r - l > 1:
	m = (l + r) // 2
	v = 0
	for i in range(L):
		v += X_list[i] * m ** i
	if v <= M:
		l = m
	else:
		r = m
print(l - d)
