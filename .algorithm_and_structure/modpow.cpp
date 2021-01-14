long modpow(long a, long p, long d) {
	return
		p == 1 ? a % d :
		p % 2 == 0 ? modpow(a, p / 2, d) * modpow(a, p / 2, d) % d :
		modpow(a, p - 1, d) * a % d;
}

long modperm(long n, long r, long d) {
	return
		r == 0 ? 1 :
		n * modperm(n - 1, r - 1, d) % d;
}
