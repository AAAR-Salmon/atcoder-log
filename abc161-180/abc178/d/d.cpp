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
	int S;
	cin >> S;

	ll cnt = 0;
	for (int i = 1; i <= S / 3; i++) {
		ll a = S - 3 * i;
		cnt += modperm(a + i - 1, a + i - 1, DIV) * modpow(modperm(a, a, DIV), DIV - 2, DIV) % DIV * modpow(modperm(i - 1, i - 1, DIV), DIV - 2, DIV) % DIV;
		cnt %= DIV;
	}
	cout << cnt << "\n";
	return 0;
}
