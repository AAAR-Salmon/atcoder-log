#include <iostream>
using namespace std;

int main() {
	int L;
	cin >> L;
	vector<long> dp(L-12+1,0);
	dp[0] = 1;
	for (int i = 0; i < 12; i++) {
		for (int l = 1; l <= L-12; l++) {
			dp[l] = dp[l] + dp[l-1];
		}
	}
	cout << dp[L-12] << "\n";
	return 0;
}
