#include <iostream>
#include <vector>
using namespace std;

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);

	int N, M;
	cin >> N >> M;
	vector<int> a(N), b(N), c(M), d(M);
	for (int i = 0; i < N; i++) {
		cin >> a[i] >> b[i];
	}
	for (int i = 0; i < M; i++) {
		cin >> c[i] >> d[i];
	}
	for (int i = 0; i < N; i++) {
		int minj = 0;
		int mindis = abs(a[i] - c[0]) + abs(b[i] - d[0]);
		for (int j = 0; j < M; j++) {
			int dis = abs(a[i] - c[j]) + abs(b[i] - d[j]);
			if (dis < mindis) {
				minj = j;
				mindis = dis;
			}
		}
		cout << minj + 1 << "\n";
	}
	return 0;
}
