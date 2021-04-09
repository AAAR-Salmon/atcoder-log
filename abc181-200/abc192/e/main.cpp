#include <iostream>
#include <vector>
#include <queue>
#include <tuple>

using namespace std;
using ll = int64_t;
using P = pair<ll, int>;
ll INF = 1LL << 60;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int N, M, X, Y;
	cin >> N >> M >> X >> Y;

	vector<vector<tuple<int, ll, ll>>> edges(N + 1);

	for (int i = 0; i < M; i++) {
		int A, B;
		ll T, K;
		cin >> A >> B >> T >> K;
		edges[A].push_back({ B, T, K });
		edges[B].push_back({ A, T, K });
	}

	vector<ll> dp(N + 1, INF);
	priority_queue<P, vector<P>, greater<P>> q;
	q.emplace(0, X);

	while (q.size()) {
		auto [d, from] = q.top(); q.pop();
		if (dp[from] < d) {
			continue;
		}
		for (auto [to, t, k] : edges[from]) {
			ll to_d = (d + k - 1) / k * k + t;
			if (to_d < dp[to]) {
				dp[to] = to_d;
				q.emplace(to_d, to);
			}
		}
	}

	cout << (dp[Y] != INF ? dp[Y] : -1) << "\n";

	return 0;
}
