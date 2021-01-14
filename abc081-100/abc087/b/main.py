A,B,C,X = (int(input()) for _ in range(4))
ans = 0
for a in range(A+1):
	for b in range(B+1):
		if 500*a + 100*b + 50*C >= X >= 500*a + 100*b:
			ans += 1
print(ans)
