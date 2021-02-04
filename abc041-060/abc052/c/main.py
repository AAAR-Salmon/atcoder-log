MOD = 1000000007

N = int(input())
primes = set()
for i in range(2, N+1):
	iisprime = True
	for j in primes:
		if i % j == 0:
			iisprime = False
			break
	if iisprime:
		primes.add(i)
factor = {p:0 for p in primes}
for i in range(1, N+1):
	for p in primes:
		if i % p == 0:
			while i % p == 0:
				factor[p] += 1
				i //= p
ans = 1
for v in factor.values():
	ans *= v+1
	ans %= MOD
print(ans)
