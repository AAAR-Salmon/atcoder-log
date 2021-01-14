#include <iostream>
#include <vector>
using namespace std;
using ll = long long;

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);

	int N;
	cin >> N;
	vector<int> L(N);
	for (int i = 0; i < N; i++) {
		cin >> L[i];
	}

	int cnt = 0;
	for (int i = 0; i < N; i++) {
		for (int j = i + 1; j < N; j++) {
			for (int k = j + 1; k < N; k++) {
				if (L[i] != L[j] && L[j] != L[k] && L[k] != L[i]) {
					if (L[i] < L[j] + L[k] && L[j] < L[k] + L[i] && L[k] < L[i] + L[j]) {
						cnt++;
					}
				}
			}
		}
	}
	cout << cnt << "\n";
	return 0;
}
