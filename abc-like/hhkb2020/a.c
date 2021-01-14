#include <stdio.h>
#include <ctype.h>

int main() {
	char S, T;
	scanf("%c %c", &S, &T);
	if (S == 'N') {
		printf("%c\n", T);
	} else {
		printf("%c\n", toupper(T));
	}
	return 0;
}
