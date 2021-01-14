#include <stdio.h>

int main() {
	long long ans = 0, b = 0;
	char c;
	while ((c = getchar()) != EOF) {
		if (c == 'W') {
			ans += b;
		} else {
			b++;
		}
	}
	printf("%lld\n", ans);
	return 0;
}
