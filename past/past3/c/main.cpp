#include <stdio.h>
using namespace std;
using ll=long long;

ll MIL = 1000000000;

ll pow(ll b, ll p) {
	if (p == 0) {
		return 1;
	} else if (p > 1 && b * b > MIL) {
		return MIL + 1;
	} if (p % 2 == 0) {
		return pow(b * b, p / 2);
	} else {
		return b * pow(b, p - 1);
	}
}

int main() {
	ll A, R, N;
	scanf("%ld%ld%ld", &A, &R, &N);
	ll res;
	if ((res = A * pow(R, N - 1)) > MIL) {
		printf("large\n");
	} else {
		printf("%ld\n", res);
	}
}
