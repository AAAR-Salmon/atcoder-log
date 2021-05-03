N,P = map(int,input().split())
if N == 1:
	print(P)
elif N >= 40:
	print(1)
else:
	i = 1
	ans = 1
	while i ** N <= P:
		if P % i ** N == 0:
			ans = i
		i += 1
	print(ans)
