#include <stdio.h>

int main() {
	int N;
	scanf("%d", &N);
	printf("%d\n", (1000 - N % 1000) % 1000);
	return 0;
}
