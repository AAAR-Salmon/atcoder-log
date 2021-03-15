from functools import reduce
from operator import mul
from math import gcd
from itertools import chain

N = int(input())
X = list(map(int,input().split()))

M = 50
isprime = [True] * (M+1)
isprime[0] = isprime[1] = False
for i in chain([2], range(3, M+1, 2)):
	if not isprime[i]:
		continue
	for j in range(i*2, M+1, i):
		isprime[j] = False

primes = [i for i,v in enumerate(isprime) if v]

ans = reduce(mul, primes)
primes_len = len(primes)
for b in range(1 << primes_len):
	Y = 1
	for i in range(primes_len):
		if b >> i & 1:
			Y *= primes[i]
	satisfiable = True
	for x in X:
		if gcd(Y, x) == 1:
			satisfiable = False
			break
	if satisfiable:
		ans = min(ans, Y)

print(ans)
