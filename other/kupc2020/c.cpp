#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
using namespace std;

int main() {
	int const N = 8;
	cout << N << "\n";
	string const ALP = "abcdefghijklmnopqrstuvwxyz";
	map<char, set<char>> bic{};
	for (auto c : ALP) {
		bic.emplace(c, set<char>{});
	}
	vector<string> ans(N, "........");
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			for (auto c : ALP) {
				if (i != 0) {
					if (bic[ans[i - 1][j]].find(c) != bic[ans[i - 1][j]].end()) {
						continue;
					}
					if (j < N - 1) {
						if (c == ans[i - 1][j + 1]) {
							continue;
						}
					}
				}
				if (j != 0) {
					if (bic[ans[i][j - 1]].find(c) != bic[ans[i][j - 1]].end()) {
						continue;
					}
				}
				ans[i][j] = c;
				if (i != 0) {
					bic[ans[i - 1][j]].insert(c);
				}
				if (j != 0) {
					bic[ans[i][j - 1]].insert(c);
				}
				break;
			}
		}
	}
	for (auto row : ans) {
		cout << row << "\n";
	}
}
