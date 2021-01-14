#include <stdio.h>
#define ll long long

int main(void) {
	ll N;
	ll ans = 0;
	scanf("%lld", &N);
	for (ll j = 1; j <= N; j++) {
		ans += j * ((N / j) * (N / j + 1) / 2);
	}
	printf("%lld\n", ans);
	return 0;
}
