#include <iostream>
using namespace std;

int main() {
	int N;
	cin >> N;
	int cnt = 0;
	for (int i = 1; i <= N; i++) {
		int a;
		cin >> a;
		if (i % 2 && a % 2) {
			cnt++;
		}
	}
	cout << cnt << endl;
	return 0;
}
