#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const *argv[]) {
	int n,m,x;
	cin >> n >> m >> x;
	vector<int> c(n);
	vector<vector<int>> a(n, vector<int> (m, 0));
	for (size_t i = 0; i < n; i++) {
		cin >> c.at(i);
		for (size_t j = 0; j < m; j++) {
			cin >> a.at(i).at(j);
		}
	}

	int minval = 1300000;
	for (size_t bits = 0; bits < 1 << n; bits++) {
		bool isAchieve = true;
		for (size_t j = 0; j < m; j++) {
			int rikaido = 0;
			for (size_t i = 0; i < n; i++) {
				if ((bits >> i) & 1) {
					rikaido += a.at(i).at(j);
				}
			}
			if (rikaido < x) {
				isAchieve = false;
				break;
			}
		}
		if (isAchieve) {
			int val = 0;
			for (size_t i = 0; i < n; i++) {
				if ((bits >> i) & 1) {
					val += c.at(i);
				}
			}
			minval = min(minval, val);
		}
	}

	if (minval == 1300000) {
		cout << -1 << endl;
	} else {
		cout << minval << endl;
	}
}
