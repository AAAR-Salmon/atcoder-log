#include <iostream>
using namespace std;
using ll = long long;

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);

	int N;
	cin >> N;
	int A[100000] = {0};
	for (int i = 0; i < N; i++) {
		int a;
		cin >> a;
		A[a]++;
	}
	int maxi, cnt;
	maxi = cnt = A[0] + A[1] + A[2];
	for (int i = 0; i < 99997; i++) {
		cnt -= A[i];
		cnt += A[i + 3];
		maxi = max(maxi, cnt);
	}
	cout << maxi << "\n";
	return 0;
}
