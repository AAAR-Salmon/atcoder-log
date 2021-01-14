#include <stdio.h>
#include <string.h>

int main() {
	int dayn = 7;
	char* days[] = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
	char S[4];
	scanf("%s", S);
	for (int i = 0; i < dayn; i++) {
		if (strcmp(S, days[i]) == 0) {
			printf("%d\n", dayn - i);
		}
	}
	return 0;
}
