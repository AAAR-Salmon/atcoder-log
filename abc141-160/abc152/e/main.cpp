#include <bits/stdc++.h>

using namespace std;
using ll = long long;

const ll MOD = 1000000007LL;

template <typename T>
inline T chmax(T &target, T value) {
	return target = value > target ? value : target;
}

ll pow(ll base, ll exp) {
	if (exp == 0) {
		return 1;
	} else if (exp & 1) {
		return pow(base, exp - 1) * base % MOD;
	} else {
		return pow(base * base % MOD, exp / 2);
	}
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int N;
	cin >> N;
	vector<ll> A(N);
	ll maxA = 0;
	for (int i = 0; i < N; i++) {
		cin >> A[i];
		chmax(maxA, A[i]);
	}

	vector<ll> spf(maxA + 1);
	iota(spf.begin(), spf.end(), 0);
	for (ll i = 2; i <= maxA; i++) {
		if (spf[i] == i) {
			for (ll j = 0; j <= maxA; j += i) {
				if (spf[j] == j) {
					spf[j] = i;
				}
			}
		}
	}

	unordered_map<ll, int> lcm;
	for (auto a : A) {
		unordered_map<ll, int> pf;
		while (a > 1) {
			ll p = spf[a];
			if (pf.find(p) == pf.end()) {
				pf.emplace(p, 1);
			} else {
				pf[p]++;
			}
			a /= p;
		}
		for (auto [p, k] : pf) {
			if (lcm.find(p) == lcm.end()) {
				lcm.emplace(p, k);
			} else {
				chmax(lcm[p], k);
			}
		}
	}

	ll P = 1;
	for (auto [p, k] : lcm) {
		P *= pow(p, k);
		P %= MOD;
	}

	ll Q = 0;
	for (auto a : A) {
		Q += pow(a, MOD - 2);
		Q %= MOD;
	}

	cout << P * Q % MOD << "\n";

	return 0;
}
