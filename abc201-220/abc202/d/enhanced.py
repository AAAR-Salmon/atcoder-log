A, B, K = map(int, input().split())

def comb(n, r):
	res = 1
	for i in range(r):
		res = res * (n - i) // (i + 1)
	return res

l = 0
r = comb(A + B, A)
ans = ''
while r - l > 1:
	m = l + comb(A + B - 1, A - 1)
	if m < K:
		l = m
		ans += 'b'
		B -= 1
	else:
		r = m
		ans += 'a'
		A -= 1
print(ans + 'a' * A + 'b' * B)
