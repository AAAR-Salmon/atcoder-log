#include <iostream>
#include <string>
using namespace std;

int point(char, int, int, int);
char win(char);

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);
	int N, K;
	int R, S, P;
	string T;
	cin >> N >> K;
	cin >> R >> S >> P;
	cin >> T;
	char *q = new char[K];
	int ans = 0;
	int i = 0;
	for (; i < K; i++) {
		ans += point(T[i], R, S, P);
		q[i] = win(T[i]);
	}
	for (; i < N; i++) {
		if (q[i % K] == win(T[i])) {
			if (i + K < N) {
				q[i % K] = q[i % K] == T[i + K] ? win(win(q[i % K])) : win(q[i % K]);
			}
		} else {
			ans += point(T[i], R, S, P);
			q[i % K] = win(T[i]);
		}
	}
	cout << ans << "\n";
	return 0;
}

char win(char hand) {
	return
		hand == 'r' ? 'p' :
		hand == 's' ? 'r' : 's';
}

int point(char hand, int R, int S, int P) {
	return
		hand == 'r' ? P :
		hand == 's' ? R : S;
}
