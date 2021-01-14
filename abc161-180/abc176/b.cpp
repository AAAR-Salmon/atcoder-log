#include <iostream>
#include <string>
using namespace std;
using ll = long long;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	string N;
	cin >> N;
	int sum = 0;
	for (auto c : N) {
		sum += c - '0';
	}
	cout << (sum % 9 == 0 ? "Yes" : "No") << "\n";

	return 0;
}
