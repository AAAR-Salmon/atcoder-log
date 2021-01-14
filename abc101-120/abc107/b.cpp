#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);

	int H, W;
	cin >> H >> W;
	vector<string> grid(H);
	for (int i = 0; i < H; i++) {
		cin >> grid[i];
	}
	for (int i = H - 1; i >= 0; i--) {
		bool f = true;
		for (int j = W - 1; j >= 0; j--) {
			if (grid[i][j] == '#') {
				f = false;
				break;
			}
		}
		if (f) {
			grid.erase(grid.begin() + i);
			H--;
		}
	}
	for (int j = W - 1; j >= 0; j--) {
		bool f = true;
		for (int i = H - 1; i >= 0; i--) {
			if (grid[i][j] == '#') {
				f = false;
				break;
			}
		}
		if (f) {
			for (auto &col : grid) {
				col.erase(col.begin() + j);
			}
		}
	}
	for (auto s : grid) {
		cout << s << "\n";
	}
	return 0;
}
