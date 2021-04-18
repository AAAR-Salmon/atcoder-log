#include <bits/stdc++.h>

using namespace std;

void dfs(string &s, int pos, int len, int max);

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	int N;
	cin >> N;
	string s = string(N, 'a');
	dfs(s, 0, N, 0);
	return 0;
}

void dfs(string &s, int pos, int len, int max) {
	if (pos == len) {
		cout << s << "\n";
		return;
	}
	for (int i = 0; i < max; i++) {
		s[pos] = 'a' + i;
		dfs(s, pos + 1, len, max);
	}
	s[pos] = 'a' + max;
	dfs(s, pos + 1, len, max + 1);
}
