#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);

	int id, N, K;
	cin >> id >> N >> K;
	vector<string> S(N);
	for (int i = 0; i < N; i++) {
		cin >> S[i];
	}

	int x = ((N + 1) / 2);
	int Q = min(x * x, 10000);
	cout << Q << "\n";
	for (int i = 0; i < Q; i++) {
		cout << x << " " << x << " " << (i % K + 1) << "\n";
	}
	return 0;
}
