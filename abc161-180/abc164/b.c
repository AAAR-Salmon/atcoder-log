#include <stdio.h>

int main(int argc, char const *argv[]) {
	int a,b,c,d;
	scanf("%d%d%d%d", &a, &b, &c, &d);
	printf("%s\n", (c + b - 1) / b <= (a + d - 1) / d ? "Yes" : "No");
	return 0;
}
