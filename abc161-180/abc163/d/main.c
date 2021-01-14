#include <stdio.h>
#define DIV ((long)1e9 + 7)

int main(void) {
	long n, k;
	scanf("%ld%ld", &n, &k);
	long count = 0;
	for (long i = k; i <= n + 1; i++)
		/*
		 * long min, max;
		 * min = k * (0 + (k - 1)) / 2;
		 * max = k * (n + (n - k + 1)) / 2;
		 * count += max - min + 1;
		 * count %= DIV;
		 */
		count = (count + i * (n - i + 1) + 1) % DIV;
	printf("%ld\n", count);
	return 0;
}
