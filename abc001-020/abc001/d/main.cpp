#include <cstdio>
const int DPLEN = 24 * 12 + 2;

inline int time_to_int(int time) {
	return time / 100 * 12 + time % 100 / 5;
}

inline int int_to_time(int i) {
	return i / 12 * 100 + i % 12 * 5;
}

int dp[DPLEN];

int main() {
	int N;
	scanf("%d", &N);

	for (int i = 0; i < N; i++) {
		int s, e;
		scanf("%d-%d", &s, &e);
		++dp[time_to_int(s)];
		--dp[time_to_int(e + 4)];
	}
	for (int i = 0; i < DPLEN - 1; i++) {
		dp[i + 1] += dp[i];
	}
	int s = 0;
	for (int i = 1; i < DPLEN; i++) {
		if (dp[i - 1] == 0 && dp[i] > 0) {
			s = i;
		}
		if (dp[i - 1] > 0 && dp[i] == 0) {
			printf("%04d-%04d\n", int_to_time(s), int_to_time(i));
		}
	}


	return 0;
}
