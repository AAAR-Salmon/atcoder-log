#include <iostream>
#include <algorithm>

using namespace std;
using ll = long long;
ll H[200000];

int main() {
	int N, K;
	cin >> N >> K;
	for (int i = 0; i < N; i++) {
		cin >> H[i];
	}
	sort(H, H + N);
	ll D = 0;
	for (int i = 0; i < N - K; i++) {
		D += H[i];
	}
	cout << D << "\n";
	return 0;
}
