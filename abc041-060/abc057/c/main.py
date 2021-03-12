def d(n):
	res = 1
	while n >= 10:
		res += 1
		n //= 10
	return res

N = int(input())
ans = 12
i = 1
while i * i <= N:
	if N % i != 0:
		i += 1
		continue
	ans = min(ans, d(N // i))
	i += 1
print(ans)
