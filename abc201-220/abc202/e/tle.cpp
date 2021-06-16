#include <bits/stdc++.h>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int N;
	cin >> N;
	vector<vector<int>> parent(N);
	vector<vector<int>> children(N);
	for (int i = 1; i < N; i++) {
		int P;
		cin >> P;
		parent[i].push_back(--P);
		children[P].push_back(i);
	}

	vector<int> depth(N, -1);
	vector<vector<int>> node_has_depth(N);
	depth[0] = 0;
	node_has_depth[0].push_back(0);
	{
		stack<int> s;
		s.push(0);
		while (!s.empty()) {
			int p = s.top();
			s.pop();
			for (auto n : children[p]) {
				depth[n] = depth[p] + 1;
				node_has_depth[depth[n]].push_back(n);
				int d = depth[p];
				for (int i = 0, pi = p; 1 << i <= d; i++) {
					parent[n].push_back(parent[pi][i]);
					d -= 1 << i;
					pi = parent[pi][i];
				}
				s.push(n);
			}
		}
	}

	int Q;
	cin >> Q;
	for (int i = 0; i < Q; i++) {
		int U, D;
		cin >> U >> D;
		int d = D - depth[--U];
		if (d < 0) {
			cout << 0 << "\n";
		} else if (d == 0) {
			cout << 1 << "\n";
		} else {
			int cnt = 0;
			for (auto v : node_has_depth[D]) {
				d = D - depth[U];
				for (int i = 0; d; i++) {
					if (d & 1 << i) {
						v = parent[v][i];
						d -= 1 << i;
					}
				}
				if (v == U) {
					++cnt;
				}
			}
			cout << cnt << "\n";
		}
	}


	return 0;
}
