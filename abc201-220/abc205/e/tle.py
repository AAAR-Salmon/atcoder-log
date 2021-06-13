from sys import setrecursionlimit

setrecursionlimit(10000000)

MOD = 1000000007


def p(n, r):
	res = 1
	for i in range(r):
		res = res * (n - i) % MOD
	return res


def c(n, r):
	if n < 0:
		return 0
	return p(n, r) * pow(p(r, r), MOD - 2, MOD) % MOD


W, B, K = map(int, input().split())
ans = 0


def solve(w, b):
	if w > W or b > B or w > b + K:
		return 0
	if W <= b + K:
		return c(W + B - w - b, W - w)
	return (solve(w + 1, b) + solve(w, b + 1)) % MOD


print(solve(0, 0))
