#include <iostream>
#include <string>
using namespace std;
using ll = long long;

int main() {
	string S, T;
	cin >> S >> T;
	int count = 0;
	for (int i = 0; i < S.size(); i++) {
		if (S[i] != T[i]) {
			count++;
		}
	}
	cout << count << endl;
	return 0;
}
