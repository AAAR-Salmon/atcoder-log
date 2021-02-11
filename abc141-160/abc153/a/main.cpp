#include <bits/stdc++.h>
using namespace std
#define rep(i,r) for (int i = 0; i < r; i++)
#define repeq(i,r) for (int i = 0; i <= r; i++)
#define isc(n) scanf("%d", &n)

int main() {
	int H, A
	isc(H)
	isc(A)
	printf("%d", H / A + (H % A > 0 ? 1: 0))
	return 0
}
