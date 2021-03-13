A,B,W = map(int,input().split())
W *= 1000
if A > W:
	print('UNSATISFIABLE')
	exit(0)


l = 0
r = W // A + 5
while r - l > 1:
	m = (l + r) // 2
	if A * m <= W:
		l = m
	else:
		r = m
ans0 = l
l = 0
r = W // A + 5
while r - l > 1:
	m = (l + r) // 2
	if W <= B * m:
		r = m
	else:
		l = m
ans1 = r

if ans1 > ans0:
	print('UNSATISFIABLE')
else:
	print(ans1, ans0)

