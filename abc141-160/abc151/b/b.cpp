#include <stdio.h>

using namespace std;

int main() {
	int N, K, M;
	scanf("%d%d%d", &N, &K, &M);
	int sum = 0;
	for (int i = 0; i < N - 1; i++) {
		int A;
		scanf("%d", &A);
		sum += A;
	}
	int res = N * M - sum;
	printf("%d", res > K ? -1 : (res < 0 ? 0 : res));
}
