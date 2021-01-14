#include <iostream>
#include <vector>
using namespace std;
using ll = long long;

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);

	int H, W;
	cin >> H >> W;
	vector<string> S(H);
	for (int i = 0; i < H; i++) {
		cin >> S[i];
	}
	int cnt = 0;
	for (int i = 0; i < H; i++) {
		for (int j = 0; j < W; j++) {
			if (S[i][j] == '.') {
				if (i + 1 < H && S[i + 1][j] == '.') {
					cnt++;
				}
				if (j + 1 < W && S[i][j + 1] == '.') {
					cnt++;
				}
			}
		}
	}
	cout << cnt << "\n";
	return 0;
}
