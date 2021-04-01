def p(r,n):
	if n == 0:
		return 1
	elif n > 1 and r ** 2 > 1000000000:
		return 1000000001
	elif n % 2 == 0:
		return p(r ** 2, n // 2)
	else:
		return p(r, n - 1) * r

A,R,N = map(int,input().split())
ans = p(R, N - 1) * A
if ans > 1000000000:
	print('large')
else:
	print(ans)
