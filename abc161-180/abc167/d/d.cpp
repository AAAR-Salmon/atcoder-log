#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main(int argc, char const *argv[]) {
	ll n;
	ll k;
	cin >> n >> k;
	vector<int> a(n + 1);
	vector<ll> last(n + 1, 0);
	vector<int> history(n * 2);
	for (size_t i = 1; i <= n; i++) {
		scanf("%d", &a.at(i));
	}

	ll pos = 1;
	last.at(1) = 0;
	ll aj, loop = 0;
	for (ll i = 1; i <= k; i++) {
		pos = a.at(pos);
		if (last.at(pos) != 0) {
			aj = last.at(pos) - 1;
			loop = i - last.at(pos);
			break;
		} else {
			last.at(pos) = i;
			history.at(i) = pos;
		}
	}
	if (loop == 0) {
		cout << history.at(k) << endl;
	} else {
		cout << history.at(aj + (k - aj) % loop) << endl;
	}
}
