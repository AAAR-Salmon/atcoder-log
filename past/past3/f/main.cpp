#include <stdio.h>
#include <vector>
#include <unordered_set>
using namespace std;

int main() {
	int N;
	scanf("%d\n", &N);
	vector<unordered_set<char>> a(N);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			a.at(i).insert(getchar());
		}
		getchar();
	}

	vector<char> S(N);
	for (int i = 0; i < N / 2; i++) {
		bool ex = true;
		for (auto c : a.at(i)) {
			if (a.at(N - i - 1).find(c) != a.at(N - i - 1).end()) {
				S.at(i) = c;
				S.at(N - i - 1) = c;
				ex = false;
				break;
			}
		}
		if (ex) {
			printf("-1\n");
			return 0;
		}
	}
	if (N % 2 == 1) {
		S.at(N / 2) = *(a.at(N / 2).begin());
	}

	for (int i = 0; i < N; i++) {
		putchar(S.at(i));
	}
	putchar('\n');
	return 0;
}
