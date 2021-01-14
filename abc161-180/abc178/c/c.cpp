#include <iostream>
using namespace std;
using ll = long long;

ll modperm(ll n, ll r, ll d) {
	return
		r == 0 ? 1 :
		n * modperm(n - 1, r - 1, d) % d;
}

ll modpow(ll a, ll p, ll d) {
	return
		p == 0 ? 1 :
		p == 1 ? a % d :
		p % 2 == 0 ? modpow(a, p / 2, d) * modpow(a, p / 2, d) % d :
		modpow(a, p - 1, d) * a % d;
}

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);

	ll const DIV = 1000000007;
	int N;
	cin >> N;

	if (N < 2) {
		cout << 0 << "\n";
	} else {
		cout << (modpow(10, N, DIV) - modpow(9, N, DIV) * 2 + modpow(8, N, DIV) + DIV * 2) % DIV << "\n";
	}
	return 0;
}
