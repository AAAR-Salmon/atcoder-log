#include <iostream>
#include <vector>
using namespace std;

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);

	int N, Q;
	cin >> N >> Q;
	vector<int> A(N);
	vector<int> cums(N+1, 0);
	for (int i = 0; i < N; i++) {
		cin >> A[i];
		cums[i+1] = cums[i] ^ A[i];
	}

	vector<int> Ys(N, 0);
	for (int i = 0; i < Q; i++) {
		int T, X, Y;
		cin >> T >> X >> Y;
		if (T == 1) {
			Ys[X-1] ^= Y;
		} else {
			X--;
			Y--;
			int out = cums[Y+1] ^ cums[X];
			for (int i = X; i <= Y; i++) {
				out ^= Ys[i];
			}
			cout << out << "\n";
		}
	}

	return 0;
}
