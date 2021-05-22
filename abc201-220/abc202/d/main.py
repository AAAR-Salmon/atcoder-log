A, B, K = map(int, input().split())

comb = [[0] * (max(A, B) + 1) for _ in range(A + B + 1)]
for n in range(A + B + 1):
	comb[n][0] = 1
	for r in range(1, max(A, B) + 1):
		comb[n][r] = comb[n - 1][r - 1] + comb[n - 1][r]

a = A
b = B
K -= 1
ans = bytearray(('a' * (A + B)).encode())
i = 0
while a + b > 0:
	if b > 0 and comb[a + b - 1][a - 1] <= K:
		ans[i] = 98
		K -= comb[a + b - 1][a - 1]
		b -= 1
	else:
		a -= 1
	i += 1
print(bytes(ans).decode())
