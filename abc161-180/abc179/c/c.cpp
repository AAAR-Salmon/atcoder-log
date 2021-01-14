#include <iostream>
using namespace std;

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);

	int N;
	cin >> N;
	int cnt = 0;
	for (int a = 1; a < N; a++) {
		cnt += (N - 1) / a;
	}
	cout << cnt << "\n";
	return 0;
}
