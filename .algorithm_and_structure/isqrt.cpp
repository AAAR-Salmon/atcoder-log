// ビット管理
ll isqrt(ll n) {
	ll i = 1;
	while (i * i < n) {
		i <<= 1;
	}
	ll res = 0;
	while (i > 0) {
		if ((res + i) * (res + i) <= n) {
			res += i;
		}
		i >>= 1;
	}
	return res;
}
