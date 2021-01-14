#include <stdio.h>
#include <set>
#include <algorithm>
using namespace std;

int main() {
	int X, N;
	scanf("%d%d", &X, &N);
	set<int> p{};
	for (int i = 0; i < N; i++) {
		int a;
		scanf("%d", &a);
		p.insert(a);
	}

	for (int i = 0; i <= N; i++) {
		if (p.find(X - i) == p.end()) {
			printf("%d\n", X - i);
			return 0;
		}
		if (p.find(X + i) == p.end()) {
			printf("%d\n", X + i);
			return 0;
		}
	}
}
