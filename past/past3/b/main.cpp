#include <stdio.h>
#include <vector>
using namespace std;

int main() {
	int N, M, Q;
	scanf("%d%d%d", &N, &M, &Q);

	vector<vector<bool>> solved(N, vector<bool> (M, false));
	vector<int> solved_count(M, 0);

	for (int i = 0; i < Q; i++) {
		int p;
		scanf("%d", &p);
		if (p == 1) {
			int n, s = 0;
			scanf("%d", &n);
			n--;
			for (int j = 0; j < M; j++) {
				if (solved.at(n).at(j)) {
					s += N - solved_count.at(j);
				}
			}
			printf("%d\n", s);
		} else {
			int n, m;
			scanf("%d%d", &n, &m);
			n--;
			m--;
			solved.at(n).at(m) = true;
			solved_count.at(m)++;
		}
	}
	return 0;
}
