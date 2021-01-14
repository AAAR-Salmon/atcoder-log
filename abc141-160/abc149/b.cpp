#include <iostream>
using namespace std;
using ll = long long int;

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);
	ll A, B, K;
	cin >> A >> B >> K;
	if (A > K) {
		A -= K;
	} else if (A + B > K) {
		B = A + B - K;
		A = 0;
	} else {
		A = B = 0;
	}
	cout << A << " " << B << "\n";
	return 0;
}
