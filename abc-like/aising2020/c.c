#include <stdio.h>

int main() {
	int N;
	scanf("%d", &N);
	for (int n = 1; n <= N; n++) {
		int cnt = 0;
		for (int i = 1; i <= 100; i++) {
			if (i * (i + 2) + 3 > n) {
				break;
			}
			for (int j = i; j <= 100; j++) {
				if (i * (i + j + 1) + j * (j + 1) + 1 > n) {
					break;
				}
				for (int k = j; k <= 100; k++) {
					if (i * (i + j + k) + j * (j + k) + k * k == n) {
						cnt++;
						if (i != k) {
							cnt += 2;
						}
						if (i != j && j != k) {
							cnt += 3;
						}
					}
				}
			}
		}
		printf("%d\n", cnt);
	}
	return 0;
}
