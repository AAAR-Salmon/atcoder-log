#include <stdio.h>
#include <vector>
#include <unordered_set>
using namespace std;

int main() {
	int N, M, Q;
	scanf("%d%d%d", &N, &M, &Q);
	vector<unordered_set<int>> adj(N);
	for (int i = 0; i < M; i++) {
		int u, v;
		scanf("%d%d", &u, &v);
		u--;
		v--;
		adj.at(u).insert(v);
		adj.at(v).insert(u);
	}
	vector<int> c(N);
	for (int i = 0; i < N; i++) {
		scanf("%d", &c.at(i));
	}

	for (int i = 0; i < Q; i++) {
		int p, x;
		scanf("%d%d", &p, &x);
		x--;
		printf("%d\n", c.at(x));
		if (p == 1) {
			for (auto adjn : adj.at(x)) {
				c.at(adjn) = c.at(x);
			}
		} else {
			int y;
			scanf("%d", &y);
			c.at(x) = y;
		}
	}
	return 0;
}
