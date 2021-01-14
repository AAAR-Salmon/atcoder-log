#include <iostream>
#include <vector>
using namespace std;
using ll = long long;

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);

	int N;
	cin >> N;
	vector<int> x(N), y(N);
	for (int i = 0; i < N; i++) {
		cin >> x[i] >> y[i];
	}
	int distance = 0;
	for (int i = 0; i < N - 1; i++) {
		distance += abs(x[i + 1] - x[i]) + abs(y[i + 1] - y[i]);
	}
	cout << distance << "\n";
	return 0;
}
