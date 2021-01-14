#include <stdio.h>
using namespace std;
using ll = long long;

int main(void) {
	ll A;
	int b1, b2;
	scanf("%lld %d.%d", &A, &b1, &b2);
	printf("%lld\n", A * (b1 * 100 + b2) /  100);
	return 0;
}
