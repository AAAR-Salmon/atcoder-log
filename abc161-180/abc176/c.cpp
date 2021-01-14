#include <iostream>
#include <vector>
#include <cmath>
using namespace std;
using ll = long long;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int N;
	cin >> N;
	vector<int> A(N), B(N);
	for (int i = 0; i < N; i++) {
		cin >> A[i];
	}
	B[0] = A[0];
	for (int i = 1; i < N; i++) {
		B[i] = max(A[i], B[i - 1]);
	}

	ll ans = 0;
	for (int i = 1; i < N; i++) {
		int d;
		if ((d = B[i - 1] - A[i]) > 0) {
			ans += d;
		}
	}

	cout << ans << "\n";
	return 0;
}
