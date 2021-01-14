#include <iostream>
using namespace std;
using ll = long long;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int N, X, T;
	cin >> N >> X >> T;
	cout << (N + X - 1) / X * T << "\n";

	return 0;
}
