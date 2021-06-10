#include <bits/stdc++.h>

using namespace std;
using ll = long long;

const ll INF = 1LL << 60;

ll isqrt(ll n) {
	ll l = -1, r = n + 1;
	while (r - l > 1) {
		ll m = (l + r) / 2;
		if (m * m <= n) {
			l = m;
		} else {
			r = m;
		}

	}
	return l;

}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int N, M;
	cin >> N >> M;
	vector<vector<tuple<int, ll, ll>>> edges(N + 1);
	for (int i = 0; i < M; i++) {
		int a, b;
		ll c, d;
		cin >> a >> b >> c >> d;
		edges[a].emplace_back(b, c, d);
		edges[b].emplace_back(a, c, d);
	}

	vector<ll> dp(N + 1, INF);
	dp[1] = 0;
	priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<pair<ll, int>>> q;
	q.emplace(0, 1);
	while (q.size()) {
		auto [t, from] = q.top();
		q.pop();
		if (t > dp[from]) {
			continue;
		}
		for (auto &&[to, c, d] : edges[from]) {
			ll s = t + c + d / (t + 1);
			ll rd = isqrt(d);
			for (ll i = max(t, rd - 1); i < rd + 1; i++) {
				s = min(s, i + c + d / (i + 1));
			}
			if (s < dp[to]) {
				dp[to] = s;
				q.emplace(s, to);
			}
		}

	}

	cout << (dp[N] == INF ? -1 : dp[N]) << "\n";

	return 0;
}


