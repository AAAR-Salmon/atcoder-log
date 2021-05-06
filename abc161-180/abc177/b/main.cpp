#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	string S, T;
	cin >> S >> T;
	int ans = T.size();
	for (int i = 0; i < S.size() - T.size() + 1; i++) {
		int cnt = 0;
		for (int j = 0; j < T.size(); j++) {
			if (S[i + j] != T[j]) {
				cnt++;
			}
		}
		ans = min(ans, cnt);
	}
	cout << ans << "\n";
	return 0;
}
