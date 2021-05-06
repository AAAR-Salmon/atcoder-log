#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	int D, T, S;
	cin >> D >> T >> S;
	cout << (D <= T * S ? "Yes" : "No") << "\n";
	return 0;
}
