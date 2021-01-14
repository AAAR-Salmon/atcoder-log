#include <iostream>
using namespace std;

int main(void) {
	cin.tie(0);
	ios::sync_with_stdio(false);

	int N, K;
	cin >> N >> K;
	bool *has = new bool[N];
	for (int i = 0; i < N; i++) {
		has[i] = false;
	}

	for (int i = 0; i < K; i++) {
		int d;
		cin >> d;
		for (int j = 0; j < d; j++) {
			int a;
			cin >> a;
			has[a-1] = true;
		}
	}

	int ans = 0;
	for (int i = 0; i < N; i++) {
		if (!has[i]) {
			ans++;
		}
	}
	cout << ans << "\n";
	return 0;
}
