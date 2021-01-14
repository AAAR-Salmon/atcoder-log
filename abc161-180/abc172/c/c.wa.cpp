#include <stdio.h>
using namespace std;
using ll = long long;

int main() {
	int N, M;
	ll K;
	scanf("%d%d%lld", &N, &M, &K);
	ll A[200000];
	int cnt, ca, cb;
	cnt = ca = cb = 0;
	ll s = 0;
	for (int i = 0; i < N; i++) {
		ll a;
		scanf("%lld", &a);
		if (s + a <= K) {
			A[i] = a;
			ca++;
			s += a;
		}
	}

	cnt = ca;
	for (int i = 0; i < M; i++) {
		ll b;
		scanf("%lld", &b);
		while (s + b > K && ca > 0) {
			s -= A[--ca];
		}
		if (s + b > K) {
			break;
		}
		s += b;
		if (ca + ++cb > cnt) {
			cnt = ca + cb;
		}
	}

	printf("%d\n", cnt);
	return 0;
}
