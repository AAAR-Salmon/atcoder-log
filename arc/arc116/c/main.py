MOD = 998244353

def modperm(n, r):
	res = 1
	for i in range(n, n - r, -1):
		res = res * i % MOD
	return res

def modcomb(n, r):
	return modperm(n, r) * pow(modperm(r, r), MOD - 2, MOD) % MOD

N,M = map(int,input().split())

SPF = [i for i in range(M + 1)]
i = 2
while i ** 2 <= M:
	if SPF[i] == i:
		for j in range(i * 2, M + 1, i):
			if SPF[j] == j:
				SPF[j] = i
	i += 1

ans = 1
for i in range(2, M + 1):
	f = {}
	an = i
	while an > 1:
		p = SPF[an]
		if p not in f:
			f[p] = 1
		else:
			f[p] += 1
		an //= p
	c = 1
	for _, v in f.items():
		c = c * modcomb(N + v - 1, v) % MOD
	ans = (ans + c) % MOD
print(ans)
