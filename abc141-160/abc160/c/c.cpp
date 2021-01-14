#include <bits/stdc++.h>
using namespace std;
#define rep(i, r) for (int i = 0; i < r; i++)

int main() {
	int K, N;
	cin >> K >> N;
	int A[N];
	rep(i, N) cin >> A[i];

	int m = A[0] + K - A[N - 1];
	rep(i, N - 1) m = max(m, A[i + 1] - A[i]);

	cout << K - m << endl;
	return 0;
}
