#include <stdio.h>
#include <vector>
using namespace std;

int main(void) {
	int N;
	scanf("%d", &N);
	vector<int> a(N + 1);
	for (int i = 1; i <= N; i++) {
		scanf("%d", &a.at(i));
	}
	vector<bool> b(N + 1, true);
	int i = 1, count = 0;
	while (b.at(i)) {
		b.at(i) = false;
		count++;
		i = a.at(i);
		if (i == 2) {
			printf("%d\n", count);
			return 0;
		}
	}
	printf("-1\n");
	return 0;
}
