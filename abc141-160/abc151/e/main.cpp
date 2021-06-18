#include <bits/stdc++.h>
#include <atcoder/all>

using namespace std;
using ll = long long;

const ll MOD = 1000000007LL;

ll fact[100001] = { 1, 1 };
ll inv[100001] = { 0, 1 };
ll finv[100001] = { 1, 1 };
void binomInit(int N) {
	for (int i = 2; i < N; i++) {
		fact[i] = fact[i - 1] * i % MOD;
		inv[i] = MOD - inv[MOD % i] * (MOD / i) % MOD;
		finv[i] = finv[i - 1] * inv[i] % MOD;
	}
}


ll binom(ll n, ll r) {
	if (n < r) {
		return 0;
	}
	return fact[n] * (finv[n - r] * finv[r] % MOD) % MOD;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int N, K;
	cin >> N >> K;
	binomInit(N + 1);
	vector<ll> A(N);
	for (int i = 0; i < N; i++) {
		cin >> A[i];
	}
	sort(A.begin(), A.end());

	ll ans = 0;
	for (int i = 0; i < N; i++) {
		ans += A[i] * binom(i, K - 1);
		ans -= A[i] * binom(N - i - 1, K - 1);
		ans %= MOD;
	}

	cout << ans << "\n";

	return 0;
}
