A, B, K = map(int, input().split())

def comb(n, r):
	res = 1
	for i in range(r):
		res = res * (n - r) // (r + 1)

a = A
b = B
K -= 1
ans = ''
i = 0
while a + b > 0:
	c = comb(a + b - 1)(a - 1)
	if b > 0 and c <= K:
		ans[i] = 98
		K -= c
		b -= 1
		ans += 'b'
	else:
		a -= 1
		ans += 'a'
	i += 1
print(ans)
