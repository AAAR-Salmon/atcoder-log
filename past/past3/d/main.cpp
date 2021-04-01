#include <stdio.h>
using namespace std;

int main() {
	int N;
	scanf("%d", &N);
	char s1[4 * N + 1], s2[4 * N + 1], s3[4 * N + 1], s4[4 * N + 1], s5[4 * N + 1];
	scanf("%s\n%s\n%s\n%s\n%s", s1, s2, s3, s4, s5);
	for (int i = 1; i <= N; i++) {
		if (s1[4 * i - 3] == '.') {
			putchar('1');
		} else if (s1[4 * i - 2] == '.') {
			putchar('4');
		} else if (s3[4 * i - 3] == '.') {
			putchar('7');
		} else if (s3[4 * i - 2] == '.') {
			putchar('0');
		} else if (s2[4 * i - 3] == '.') {
			if (s4[4 * i - 1] == '.') {
				putchar('2');
			} else {
				putchar('3');
			}
		} else if (s4[4 * i - 3] == '.') {
			if (s2[4 * i - 1] == '.') {
				putchar('5');
			} else {
				putchar('9');
			}
		} else if (s2[4 * i - 1] == '.') {
			putchar('6');
		} else {
			putchar('8');
		}
	}
	putchar('\n');
}
