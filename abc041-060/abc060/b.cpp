#include <iostream>
#include <utility>
using namespace std;
using ll = long long;

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);

	int A, B, C;
	cin >> A >> B >> C;
	while ((A %= B) != 0) {
		swap(A, B);
	}
	cout << (C % B == 0 ? "YES" : "NO") << "\n";
	return 0;
}
