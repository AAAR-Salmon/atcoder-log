#include <stdio.h>

using ll = long long;

ll modpow(ll base, ll power, ll mod) {
	if (power == 0) {
		return 1;
	} else if (power % 2 == 0) {
		return modpow(base * base % mod, power / 2, mod);
	} else {
		return base * modpow(base, power - 1, mod) % mod;
	}
}

int main(int argn, char *argv[]) {
	ll N, M, P;
	scanf("%ld%ld%ld", &N, &M, &P);
	printf("%ld\n", modpow(N, P, M));
	return 0;
}
