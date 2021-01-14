#include <iostream>
#include <set>
using namespace std;

int main() {
	set<int> P = {};
	int X;
	cin >> X;
	for (int i = 2; i < 1000000; i++) {
		bool isPrime = true;
		for (auto p : P) {
			if (i % p == 0) {
				isPrime = false;
				break;
			}
		}
		if (isPrime) {
			if (i >= X) {
				cout << i << "\n";
				break;
			} else {
				P.insert(i);
			}
		}
	}
}
