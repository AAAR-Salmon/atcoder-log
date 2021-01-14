#include <iostream>
using namespace std;
using ll = long long;

int main() {
	int N;
	ll D;
	cin >> N >> D;
	int cnt = 0;
	for (int i = 0; i < N; i++) {
		ll X, Y;
		cin >> X >> Y;
		if (X * X + Y * Y <= D * D) {
			cnt++;
		}
	}
	cout << cnt << endl;
	return 0;
}
