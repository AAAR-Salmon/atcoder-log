#include <stdio.h>

#define rep(i,r) for(int i=0;i<r;i++)

int main() {
	int N;
	scanf("%d", &N);
	char S[N];
	scanf("%s", &S);
	int rgb[3] = {0};
	rep(i,N) rgb[S[i] == 'R' ? 0 : (S[i] == 'G' ? 1 : 2)]++;

	long count = (long)rgb[0] * rgb[1] * rgb[2];
	for (int i = 0; i < N - 2; i++) {
		for (int j = 1; i + j * 2 < N; j++) {
			if (S[i] != S[i + j]
				&& S[i] != S[i + j * 2]
				&& S[i + j] != S[i + j * 2]) count--;
		}
	}

	printf("%ld", count);
	return 0;
}
