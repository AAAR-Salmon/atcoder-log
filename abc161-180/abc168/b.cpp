#include <iostream>
#include <string>

using namespace std;

int main() {
	int K;
	string S;
	cin >> K >> S;
	if (S.size() > K) {
		S = S.substr(0, K);
		cout << S << "..." << endl;
	} else {
		cout << S << endl;
	}
}
