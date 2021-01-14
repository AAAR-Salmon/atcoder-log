#include <stdio.h>
#include <algorithm>
using namespace std;
using ll = long long;

int main() {
	int N, K;
	scanf("%d%d", &N, &K);
	vector<int> p(N);
	for (int i = 0; i < N; i++) {
		scanf("%d", &p.at(i));
	}
	sort(p.begin(), p.end());
	int ans = 0;
	for (int i = 0; i < K; i++) {
		ans += p.at(i);
	}
	printf("%d\n", ans);
	return 0;
}
