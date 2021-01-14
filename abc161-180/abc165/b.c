#include <stdio.h>
#define rep(i, n) for (int i = 0; i < n; i++)
#define ll long long

int main(void) {
	ll x,y = 100;
	scanf("%ld", &x);
	for (int i = 1;; i++) {
		y += y / 100;
		if (y >= x) {
			printf("%d\n", i);
			return 0;
		}
	}
}
