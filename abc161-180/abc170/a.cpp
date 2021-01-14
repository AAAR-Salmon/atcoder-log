#include <stdio.h>

int main() {
	for (int i = 1; i <= 5; i++) {
		int x;
		scanf("%d", &x);
		if (x == 0) {
			printf("%d\n", i);
		}
	}
	return 0;
}
