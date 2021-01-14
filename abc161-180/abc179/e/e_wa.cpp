#include <iostream>
#include <vector>
using namespace std;
using ll = long long;

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);

	ll N, X, M;
	cin >> N >> X >> M;
	vector<ll> A(M);
	A[0] = X;
	ll a, b;
	bool f = false;
	for (ll i = 0; i < M - 1; i++) {
		A[i + 1] = A[i] * A[i] % M;
		for (int j = 0; j < i + 1; j++) {
			if (A[j] == A[i + 1]) {
				a = j;
				b = i + 1;
				f = true;
				break;
			}
		}
		if (f) {
			break;
		}
	}

	ll ans = 0;
	if (N < b) {
		for (int i = 0; i < N; i++) {
			ans += A[i];
		}
	} else {
		ll l = b - a;
		vector<ll> sl(l); // sumloop
		sl[0] = A[a];
		for (int i = 0; i < l - 1; i++) {
			sl[i + 1] = sl[i] + A[a + i + 1];
		}

		for (ll i = 0; i < a; i++) {
			ans += A[i];
		}
		ans += (N - 1 - a) / l * sl[l - 1] + sl[(N - 1 - a) % l];
	}
	cout << ans << "\n";
	return 0;
}
