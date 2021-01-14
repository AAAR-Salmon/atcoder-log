#include <stdio.h>

int main(void) {
	int n,m,a;
	scanf("%d%d\n", &n,&m);
	for (int i = 0; i < m; i++) {
		scanf("%d", &a);
		n -= a;
	}

	printf("%d\n", n >= 0 ? n : -1);

	return 0;
}
