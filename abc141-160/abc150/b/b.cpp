#include <stdio.h>

int main() {
	int ans = 0, stat = 0;
	int N;
	scanf("%d\n", &N);
	char c;
	for (int i = 0; i < N; i++) {
		c = getchar();
		if (c == 'A') {
			stat = 1;
		} else if (c == 'A' + stat) {
			if (c == 'C') {
				ans++;
				stat = 0;
			} else {
				stat++;
			}
		} else {
			stat = 0;
		}
	}
	printf("%d\n", ans);
}
