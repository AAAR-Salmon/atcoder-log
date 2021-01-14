#include <iostream>
#include <string>
using namespace std;

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);

	int N;
	cin >> N;
	int cnt = 0;
	for (int i = 0; i < N; i++) {
		int d1, d2;
		cin >> d1 >> d2;
		if (d1 == d2) {
			if (++cnt >= 3) {
				cout << "Yes" << "\n";
				return 0;
			}
		} else {
			cnt = 0;
		}
	}
	cout << "No" << "\n";
	return 0;
}
