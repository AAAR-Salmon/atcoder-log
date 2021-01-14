#include <bits/stdc++.h>
using namespace std;
using ll = long long;
ll const MOD = 1000000007;

struct HashPair {
	std::size_t operator()(const pair<int, int> &key) const {
		return key.first * 100000 + key.second;
	}
};

vector<vector<int>> adj(100005);
vector<bool> done(100005, false);
vector<vector<int>> used_color(100005);
vector<int> last_used_color(100005, 0);
vector<pair<int, int>> edge;
unordered_map<pair<int, int>, int, HashPair> edge_color(100005);

int main() {
	int N;
	cin >> N;
	for (int i = 0; i < N-1; i++) {
		int a,b;
		cin >> a >> b;
		a--;
		b--;
		edge.push_back(make_pair(a, b));
		adj[a].push_back(b);
		adj[b].push_back(a);
	}
	int K = 0;
	for (auto a : adj) {
		K = max(K, (int)a.size());
	}
	cout << K << "\n";
	queue<int> q;
	q.push(0);
	while (!q.empty()) {
		int n = q.front();
		q.pop();
		done[n] = true;
		for (auto a : adj[n]) {
			if (done[a]) {
				continue;
			}
			q.push(a);
			int c = last_used_color[n];
			if (find(used_color[n].begin(), used_color[n].end(), ++c) != used_color[n].end()) {
				c++;
			}
			edge_color.emplace(make_pair(n,a), c);
			edge_color.emplace(make_pair(a,n), c);
			used_color[n].push_back(c);
			used_color[a].push_back(c);
			last_used_color[n] = c;
		}
	}
	for (int i = 0; i < N-1; i++) {
		cout << edge_color[edge[i]] << "\n";
	}
	return 0;
}
