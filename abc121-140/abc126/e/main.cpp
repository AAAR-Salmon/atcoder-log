#include <bits/stdc++.h>
#include <atcoder/all>

using namespace std;
using namespace atcoder;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int N, m;
	cin >> N >> m;
	dsu uf(N);

	for (int i = 0; i < m; i++) {
		int X, Y, Z;
		cin >> X >> Y >> Z;
		uf.merge(--X, --Y);
	}

	cout << uf.groups().size() << "\n";

	return 0;
}
