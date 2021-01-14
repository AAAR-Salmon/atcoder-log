#include <iostream>
#include <cmath>
using namespace std;
using ll = long long;

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);

	ll a, b, c, d;
	cin >> a >> b >> c >> d;
	cout << max(a * c, max(a * d, max(b * c, b * d))) << "\n";
	return 0;
}
