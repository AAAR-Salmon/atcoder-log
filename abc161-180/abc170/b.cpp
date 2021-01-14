#include <stdio.h>

int main() {
	int X, Y;
	scanf("%d%d", &X, &Y);
	if (Y % 2 != 0) {
		printf("No\n");
	} else if (Y < 2 * X || 4 * X < Y) {
		printf("No\n");
	} else {
		printf("Yes\n");
	}
	return 0;
}
