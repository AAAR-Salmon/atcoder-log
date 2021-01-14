#include <stdio.h>
#define ll long long

int main(void) {
	ll a, b, n;
	scanf("%ld%ld%ld", &a, &b, &n);

	// (A * x - (A * x % B)) / B - A * (x - x % B) / B
	ll x = (n >= b ? n / b * b - 1 : n);
	printf("%ld\n", (a * x) / b - a * (x / b));
	return 0;
}
