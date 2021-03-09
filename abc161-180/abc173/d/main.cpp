#include <stdio.h>
#include <algorithm>
using namespace std;
using ll = long long;

int main() {
	int N;
	scanf("%d", &N);
	ll A[N];
	for (int i = 0; i < N; i++) {
		scanf("%lld", &A[i]);
	}
	sort(A, A + N);
	ll c = A[--N];
	for (int i = --N; i > (N + 1) / 2; i--) {
		c += A[i] * 2;
	}
	if (N % 2) {
		c += A[N / 2];
	}

	printf("%lld\n", c);

	return 0;
}
