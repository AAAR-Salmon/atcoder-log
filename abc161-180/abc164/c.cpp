#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const *argv[]) {
	int n;
	unordered_set<string> s;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		char a[10];
		scanf("%s", a);
		s.insert(a);
	}

	printf("%d", s.size());
	return 0;
}
