from sys import setrecursionlimit

setrecursionlimit(1000000)

MOD = 1_000_000_007


def binom(n, r):
	r = min(r, n - r)
	a = b = 1
	for i in range(r):
		a *= n - i
		b *= i + 1
		a %= MOD
		b %= MOD
	return a * pow(b, MOD - 2, MOD) % MOD


w, h = map(int, input().split())
print(binom(w + h - 2, w - 1))
