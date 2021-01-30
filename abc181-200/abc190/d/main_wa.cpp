#include <iostream>
#include <vector>
using namespace std;
using ll = long long;

int main() {
	ll N;
	cin >> N;

	vector<ll> d;
	for (ll i = 1; i * (i + 1) <= 4 * N; i++) {
		if (2 * N % i == 0) {
			d.push_back(i);
		}
	}
	int ans = 0;
	for (auto i : d) {
		ll ok = 0;
		ll ng = N / i + 1;
		while (ng - ok > 1) {
			ll mid = (ok + ng) / 2;
			if (i * (2 * mid + i - 1) / 2 <= N) {
				ok = mid;
			} else {
				ng = mid;
			}
		}
		if (i * (2 * ok + i - 1) / 2 == N) {
			ans += 2;
		}
	}
	cout << ans << "\n";

	return 0;
}
