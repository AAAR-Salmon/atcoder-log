#include <iostream>
using namespace std;

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);

	int N;
	cin >> N;
	int *a = new int[N];
	int sum = 0;
	for (int i = 0; i < N; i++) {
		cin >> a[i];
		sum += a[i];
	}
	int ans = 0;
	int d = abs(a[0] * N - sum);
	for (int i = 1; i < N; i++) {
		if (abs(a[i] * N - sum) < d) {
			ans = i;
			d = abs(a[i] * N - sum);
		}
	}
	free(a);
	cout << ans << "\n";
	return 0;
}
