#include <iostream>
#include <string>
using namespace std;
using ll = long long;

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);

	int N;
	string S, T = "";
	string ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	cin >> N >> S;

	for (auto c : S) {
		T += ALPHABET[(c - 'A' + N) % 26];
	}
	cout << T << "\n";
	return 0;
}
