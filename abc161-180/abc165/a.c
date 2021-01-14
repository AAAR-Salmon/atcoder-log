#include <stdio.h>
#define rep(i, n) for (int i = 0; i < n; i++)

int main(void) {
	int k, a, b;
	scanf("%d%d%d", &k, &a, &b);
	for (; a <= b; a++)
		if (a % k == 0) {
			printf("OK\n");
			return 0;
		}
	printf("NG\n");
	return 0;
}
