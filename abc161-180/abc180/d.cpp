#include <iostream>
using namespace std;
using ll = long long;

bool AX_lt_Y(ll A, ll X, ll Y) {
	return X < Y / A || (X == Y / A && Y % A != 0);
}

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);

	ll X, Y, A, B;
	cin >> X >> Y >> A >> B;
	ll exp = 0;
	while (AX_lt_Y(A, X, Y) || X + B < Y) {
		if (AX_lt_Y(A - 1, X, B)) {
			X *= A;
			exp++;
		} else {
			exp += (Y - X - 1) / B;
			break;
		}
	}
	cout << exp << "\n";
	return 0;
}
