A, B, C = map(int, input().split())
p = pow(B, C, 4)
if p == 0:
	p = 4
print(pow(A, p, 10))
