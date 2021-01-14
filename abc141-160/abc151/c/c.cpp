#include <stdio.h>
#include <string.h>
#include <vector>

int main() {
	int N, M;
	scanf("%d%d", &N, &M);
	std::vector<bool> ACed(N + 1, false);
	std::vector<int> WAed(N + 1, 0);
	int AC, WA;
	AC = WA = 0;
	for (int i = 0; i < M; i++) {
		int p;
		char S[2];
		scanf("%d%s", &p, S);
		if (!ACed.at(p)) {
			if (strcmp(S, "AC") == 0) {
				AC++;
				WA += WAed.at(p);
				ACed.at(p) = true;
			} else {
				WAed.at(p)++;
			}
		}
	}
	printf("%d %d\n", AC, WA);
}
