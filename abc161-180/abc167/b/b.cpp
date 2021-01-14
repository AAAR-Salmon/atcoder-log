#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const *argv[]) {
	int n,m,x;
	cin >> n >> m >> x;
	vector<int> c(n);
	vector<vector<int>> a = vector<int> (n, vector<int> (m, 0));
	for (size_t i = 0; i < n; i++) {
		cin >> c.at(i);
		for (size_t j = 0; j < m; j++) {
			cin >> a.at(i).at(j);
		}
	}
}
