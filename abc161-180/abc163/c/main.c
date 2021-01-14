#include <stdio.h>

int main(void) {
	int n = 0;
	scanf("%d\n", &n);
	int a;
	int b[(int)2e5+1] = {0};
	for (int i = 0; i < n - 1; i++) {
		scanf("%d", &a);
		b[a]++;
	}
	for (int i = 1; i <= n; i++) {
		printf("%d\n", b[i]);
	}
	return 0;
}
