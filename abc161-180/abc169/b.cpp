#include <stdio.h>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;
using ll = long long;

int digit(ll num) {
	if (num < 10) {
		return 1;
	} else {
		return 1 + digit(num / 10);
	}
}

int main(void) {
	int N;
	scanf("%d", &N);
	ll res = 1;
	vector<ll> v(N);
	for (int i = 0; i < N; i++) {
		scanf("%ld", &v.at(i));
	}
	sort(v.begin(), v.end());
	if (v.at(0) == 0) {
		printf("0\n");
		return 0;
	}
	for (int i = 0; i < N; i++) {
		if (log10(res) + log10(v.at(i)) > 18) {
			printf("-1\n");
			return 0;
		}
		res *= v.at(i);
	}
	if (res > 1000000000000000000) {
		printf("-1\n");
		return 0;
	}
	printf("%ld\n", (ll) res);
	return 0;
}
