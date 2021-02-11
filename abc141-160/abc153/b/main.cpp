#include <bits/stdc++.h>
using namespace std;
#define rep(i,r) for (int i = 0; i < r; i++)
#define repeq(i,r) for (int i = 0; i <= r; i++)
#define isc(n) scanf("%d", &n)

int main() {
	int H, N;
	isc(H); isc(N);
	int D;
	rep(i, N) {
		int A;
		isc(A);
		D += A;
	}
	cout << (D >= H ? "Yes" : "No") << endl;

	return 0;
}
