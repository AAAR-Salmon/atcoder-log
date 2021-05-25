#include <bits/stdc++.h>
#include <atcoder/all>

using namespace std;
using namespace atcoder;
using ll = long long;
using P = pair<int, int>;

template <typename T>
T max(T a, T b) {
	return a < b ? b : a;
}

P e() {
	return make_pair<int, int>(0, 0);
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int N, M;
	cin >> N >> M;

	vector<priority_queue<P, vector<P>>> work(M + 1);
	for (int i = 0; i < N; i++) {
		int A, B;
		cin >> A >> B;
		if (A <= M) {
			work[A].emplace(B, A);
		}
	}

	segtree<P, max, e> st(M + 1);
	for (int i = 0; i <= M; i++) {
		if (!work[i].empty()) {
			st.set(i, work[i].top());
		}
	}

	int ans = 0;
	for (int d = M - 1; d >= 0; d--) {
		auto [B, A] = st.prod(0, M - d + 1);
		if (A != 0) {
			ans += B;
			// cerr << B << " " << A << "\n";
			work[A].pop();
			st.set(A, work[A].empty() ? e() : work[A].top());
		}
	}

	cout << ans << endl;

	return 0;
}
