#include <stdio.h>

int main() {
	int ans = 0;
	int N;
	scanf("%d\n", &N);
	char s[N];
	scanf("%s\n", s);
	char search[] = "ABC";
	for (int i = 0; i < N - 2; i++) {
		bool f = true;
		for (int j = 0; j < 3; j++) {
			if (s[i + j] != search[j]) {
				f = false;
				break;
			}
		}
		if (f) ans++;
	}
	printf("%d\n", ans);
}
