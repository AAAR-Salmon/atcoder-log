#include <iostream>
#include <string>
using namespace std;

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);
	string S;
	cin >> S;
	if (S[S.size() - 1] == 's') {
		cout << (S + "es") << "\n";
	} else {
		cout << (S + "s") << "\n";
	}
	return 0;
}
