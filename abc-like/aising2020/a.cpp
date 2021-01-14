#include <iostream>
using namespace std;

int main() {
	int L, R, d;
	cin >> L >> R >> d;
	cout << R / d - (L + d - 1) / d + 1 << endl;
	return 0;
}
