#include <stdio.h>

long lpow2(long num) {
	return
		num == 0 ? 1
		: num % 2 == 0 ? lpow2(num / 2) * lpow2(num / 2)
		: 2 * lpow2(num - 1);
}

int main() {
	long H;
	scanf("%ld", &H);
	int r;
	while (H > 0) {
		H /= 2;
		r++;
	}
	printf("%ld", lpow2(r) - 1);
	return 0;
}
