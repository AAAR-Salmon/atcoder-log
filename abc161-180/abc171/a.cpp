#include <stdio.h>

int main() {
	int c = getchar();
	if ('A' <= c && c <= 'Z') {
		putchar('A');
	}
	if ('a' <= c && c <= 'z') {
		putchar('a');
	}
	return 0;
}
