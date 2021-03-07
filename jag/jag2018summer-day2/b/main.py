N = int(input())
if N > 4+1+4+1+4:
	print(5*2*5*2*5)
else:
	ans = 0
	for c in range(500 * N + 1):
		if c // 500 \
			+ c % 500 // 100 \
			+ c % 100 // 50 \
			+ c % 50 // 10 \
			+ c % 10 // 5 \
			+ c % 5 == N:
			ans += 1
	print(ans)
