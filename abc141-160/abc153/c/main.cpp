#include <stdio.h>
#include <algorithm>
#define rep(i,r) for (int i = 0; i < r; i++)

using namespace std;

int main() {
	int N, K;
	scanf("%d%d", &N, &K);
	int H[N];
	rep(i, N) scanf("%d", &H[i]);
	sort(H, H + N);
	long D = 0;
	rep(i, N - K) D += H[i];
	printf("%ld", D);
	return 0;
}
