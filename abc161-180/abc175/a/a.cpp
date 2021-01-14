#include <iostream>
#include <string>
using namespace std;
using ll = long long;

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);

	string S;
	cin >> S;
	int cnt = 0, ans = 0;
	for (int i = 0; i < 3; i++) {
		if (S[i] == 'R') {
			cnt++;
			if (ans < cnt) {
				ans = cnt;
			}
		} else {
			cnt = 0;
		}
	}
	cout << ans << "\n";
	return 0;
}
