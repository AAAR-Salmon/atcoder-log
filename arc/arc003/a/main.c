#include <stdio.h>

int main() {
	int N;
	char r[101];
	double gps = 0;
	scanf("%d%s", &N, r);
	for (int i = 0; i < N; i++) {
		gps += r[i] == 'F' ? 0 : 'A' + 4 - r[i];
	}
	printf("%.15f\n", gps / N);
}
