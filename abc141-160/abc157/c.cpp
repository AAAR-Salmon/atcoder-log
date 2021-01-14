#include <iostream>
#include <vector>

using namespace std;

int ipow10(int x) {
	return x == 0 ? 1 : 10 * ipow10(x - 1);
}

int main(void) {
	int N, M;
	cin >> N >> M;
	vector<int> dec(N + 1, 0);
	vector<bool> defined(N + 1, false);
	for (int i = 0; i < M; i++) {
		int s, c;
		cin >> s >> c;
		if (defined.at(s) && dec.at(s) != c || N != 1 && s == 1 && c == 0) {
			cout << -1 << endl;
			return 0;
		} else {
			dec.at(s) = c;
			defined.at(s) = true;
		}
	}

	if (N != 1 && !defined.at(1)) dec.at(1) = 1;

	int ans = 0;
	for (int i = 1; i <= N; i++) {
		ans += dec.at(i) * ipow10(N - i);
	}
	cout << ans << endl;
	return 0;
}
