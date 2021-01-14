#include <iostream>
using namespace std;

int isqrt(int n) {
	int i = 1;
	while (i * i < n) {
		i <<= 1;
	}
	int res = 0;
	while (i > 0) {
		if ((res + i) * (res + i) <= n) {
			res += i;
		}
		i >>= 1;
	}
	return res;
}

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);

	int N;
	cin >> N;
	int cnt = 0;
	for (int c = 1; c < N; c++) {
		int ab = N - c;
		for (int a = 1; a <= isqrt(ab); a++) {
			if (ab % a == 0) {
				if (a * a == ab) {
					cnt++;
				} else {
					cnt += 2;
				}
			}
		}
	}
	cout << cnt << "\n";
	return 0;
}
