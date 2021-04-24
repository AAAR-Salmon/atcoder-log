#include <bits/stdc++.h>
#include <atcoder/all>

using namespace std;
using namespace atcoder;
using ll = long long;

vector<vector<int>> edges;
vector<int> color;
ll dfs(int i, int size, vector<int> &g);

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int N, M;
	cin >> N >> M;

	edges = vector<vector<int>>(N);
	color = vector<int>(N, -1);
	auto uf = dsu(N);

	for (int i = 0; i < M; i++) {
		int A, B;
		cin >> A >> B;
		A--;
		B--;
		uf.merge(A, B);
		edges[A].push_back(B);
		edges[B].push_back(A);
	}

	ll ans = 1;

	for (auto g : uf.groups()) {
		color[g[0]] = 0;
		ll cnt = dfs(1, g.size(), g);
		ans *= cnt * 3;
		if (cnt == 0) {
			break;
		}
	}

	cout << ans << endl;

	return 0;
}

ll dfs(int i, int size, vector<int> &g) {
	if (i == size) {
		return 1;
	}
	int v = g[i];
	ll res = 0;
	for (int c = 0; c < 3; c++) {
		bool ok = true;
		for (auto u : edges[v]) {
			if (c == color[u]) {
				ok = false;
				break;
			}
		}
		if (!ok) {
			continue;
		}
		color[v] = c;
		res += dfs(i + 1, size, g);
		color[v] = -1;
	}
	return res;
}
