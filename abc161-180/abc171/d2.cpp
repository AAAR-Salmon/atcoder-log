#include <stdio.h>

int main() {
	int N;
	scanf("%d", &N);
	int A[100000 + 1] = {0};
	long long S = 0;
	for (int i = 0; i < N; i++) {
		int a;
	 	scanf("%d", &a);
		A[a]++;
		S += a;
	}

	int Q;
	scanf("%d", &Q);
	for (int i = 0; i < Q; i++) {
		int B, C;
		scanf("%d%d", &B, &C);
		printf("%lld\n", S += (C - B) * A[B]);
		A[C] += A[B];
		A[B] = 0;
	}
	return 0;
}
