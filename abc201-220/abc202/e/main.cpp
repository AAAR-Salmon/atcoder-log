#include <bits/stdc++.h>

using namespace std;

vector<int> parent;
vector<vector<int>> children;
vector<int> depth;
vector<int> in;
vector<int> out;
vector<vector<int>> d_in;

int t = 0;
void eulerTour(int node, int d) {
	depth[node] = d;
	in[node] = t++;
	d_in[d].push_back(in[node]);
	for (auto &&child : children[node]) {
		eulerTour(child, d + 1);
	}
	out[node] = t++;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int N;
	cin >> N;
	parent.resize(N);
	children.resize(N);
	depth.resize(N);
	in.resize(N);
	out.resize(N);
	d_in.resize(N);

	parent[0] = -1;
	for (int i = 1; i < N; i++) {
		int P;
		cin >> P;
		P--;
		parent[i] = P;
		children[P].push_back(i);
	}

	eulerTour(0, 0);

	int Q;
	cin >> Q;
	for (int i = 0; i < Q; i++) {
		int U, D;
		cin >> U >> D;
		U--;

		int l, r, m;
		l = -1;
		r = d_in[D].size();
		while (r - l > 1) {
			m = (l + r) / 2;
			if (d_in[D][m] >= in[U]) {
				r = m;
			} else {
				l = m;
			}
		}
		int L = r;

		l = -1;
		r = d_in[D].size();
		while (r - l > 1) {
			m = (l + r) / 2;
			if (d_in[D][m] < out[U]) {
				l = m;
			} else {
				r = m;
			}
		}
		int R = r;
		cout << R - L << "\n";
	}

	return 0;
}
