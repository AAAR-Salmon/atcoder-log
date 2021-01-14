#include <stdio.h>
#include <math.h>
using ll = long long;

ll modpow(ll base, ll pow, ll mod) {
	if (pow == 1) {
		return base % mod;
	} else if (pow & 1) {
		return base * modpow(base * base % mod, (pow - 1) / 2, mod) % mod;
	} else {
		return modpow(base * base % mod, pow / 2, mod);
	}
}

int main() {
	ll const DIV = 1000000009;
	ll N;
	scanf("%ld", &N);
	ll ans = modpow(2, N, DIV) - 1;
	for (ll i = 0; i < N; i++) {
		ll A, B;
		scanf("%ld%ld", &A, &B);
	}
	printf("%ld\n", ans);
}
