#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int N;
	cin >> N;
	vector<pair<double, double>> p(N);
	for (int i = 0; i < N; i++) {
		cin >> p[i].first >> p[i].second;
	}
	double ans = 0.0;
	for (int i = 0; i < N; i++) {
		auto [xi, yi] = p[i];
		for (int j = 0; j < i; j++) {
			auto [xj, yj] = p[j];
			ans = max(ans, sqrt((xj - xi) * (xj - xi) + (yj - yi) * (yj - yi)));
		}
	}

	cout << ans << endl;
	return 0;
}
