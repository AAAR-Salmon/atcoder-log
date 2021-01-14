#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define ll long long

int main() {
	ll N;
	scanf("%lld", &N);

	// Lを求めつつ、Nのいらない部分をカット
	int L = 0;
	for (ll p = 1; N >= p; L++, p *= 26) { N -= p; }

	// 名前を'a'埋め文字列として生成
	char* name = (char*)malloc((L + 1) * sizeof(char));
	name[L] = '\0';
	memset(name, 'a', L);

	// 下の桁から順に置き換えていく
	for (int i = L; N > 0;) {
		name[--i] = (char) ('a' + N % 26);
		N /= 26;
	}

	printf("%s\n", name);
	return 0;
}
