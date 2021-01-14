#include <bits/stdc++.h>
using namespace std;
#define rep(i, r) for (int i = 0; i < r; i++)

int main() {
	short A[3][3];
	rep(i, 3) {
		rep(j, 3) {
			cin >> A[i][j];
		}
	}
	short N;
	cin >> N;
	short b[N];
	rep(i, N) {
		cin >> b[i];
	}

	bool opened[3][3] = {{false}};
	rep(i, 3) {
		rep(j, 3) {
			rep(k, N) {
				if (A[i][j] == b[k]) {
					opened[i][j] = true;
				}
			}
		}
	}

	rep(i, 3) {
		if (opened[i][0] && opened[i][1] && opened[i][2]) {
			cout << "Yes" << endl;
			return 0;
		}
		if (opened[0][i] && opened[1][i] && opened[2][i]) {
			cout << "Yes" << endl;
			return 0;
		}
		if (opened[0][0] && opened[1][1] && opened[2][2]) {
			cout << "Yes" << endl;
			return 0;
		}
		if (opened[2][0] && opened[1][1] && opened[0][2]) {
			cout << "Yes" << endl;
			return 0;
		}
	}
	cout << "No" << endl;
	return 0;
}
