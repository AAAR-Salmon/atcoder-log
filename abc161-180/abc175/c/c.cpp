#include <iostream>
#include <cmath>
using namespace std;
using ll = long long;

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);

	ll X, K, D;
	cin >> X >> K >> D;
	X = abs(X);
	if (X / D > K) {
		cout << X - K * D << "\n";
	} else {
		ll i = X / D;
		if ((K - i) % 2 == 0) {
			cout << X - i * D << "\n";
		} else {
			cout << D - (X - i * D) << "\n";
		}
	}
	return 0;
}
