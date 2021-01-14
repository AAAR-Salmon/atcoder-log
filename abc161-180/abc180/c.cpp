#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
using ll = long long;

ll isqrt(ll n) {
	ll i = 1;
	while (i * i < n) {
		i <<= 1;
	}
	ll res = 0;
	while (i > 0) {
		if ((res + i) * (res + i) <= n) {
			res += i;
		}
		i >>= 1;
	}
	return res;
}

int main() {
	ll N;
	scanf("%lld", &N);
	ll n = isqrt(N);
	vector<ll> ans;
	for (ll i = 1; i <= n; i++) {
		if (N % i == 0) {
			ans.push_back(i);
		}
	}

	for (auto e : ans) {
		cout << e << "\n";
	}
	reverse(ans.begin(), ans.end());
	for (auto e : ans) {
		if (e * e != N) {
			cout << N / e << "\n";
		}
	}
	return 0;
}
