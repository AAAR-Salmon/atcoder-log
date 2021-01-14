#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

int main(void) {
	cin.tie(0);
	ios::sync_with_stdio(false);

	int N, M;
	cin >> N >> M;
	int h[N];
	vector<set<int>> con(N, set<int>());
	for (int i = 0; i < N; i++) {
		cin >> h[i];
	}

	for (int i = 0; i < M; i++) {
		int a, b;
		cin >> a >> b;
		con[a-1].insert(b-1);
		con[b-1].insert(a-1);
	}

	int ans = 0;
	for (int i = 0; i < N; i++) {
		auto hst = max_element(con[i].begin(), con[i].end(), [&h](int a, int b) {
			return h[a] < h[b];
		});
		ans += hst == con[i].end() || h[i] > h[*hst];
	}
	cout << ans << "\n";
	return 0;
}
