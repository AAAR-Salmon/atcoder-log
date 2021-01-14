#include <stdio.h>
#include <stdlib.h>

int main(int argn, char *argv[]) {
	char S[3];
	int ans;
	for (int i = 0; i < 3; i++) {
		if (S[i] < '0' || '9' < S[i]) {
			printf("error\n");
			return 0;
		}
	}
	printf("%d\n", atoi(S) * 2);
}
