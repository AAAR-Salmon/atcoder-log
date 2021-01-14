#include <iostream>
#include <vector>
using namespace std;
using ll = long long;

int main(int argc, char const *argv[]) {
	ll const P = 200003;

	int N;
	cin >> N;
	vector<ll> A(N);
	ll sum = 0;
	for (int i = 0; i < N; i++) {
		cin >> A[i];
		for (int j = 0; j < i; j++) {
			sum += A[j] * A[i] % P;
		}
	}
	cout << sum << endl;
	return 0;
}
