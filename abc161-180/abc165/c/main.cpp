#include <iostream>
using namespace std;
using ll = long long;

int N, M, Q;
int a[50], b[50], c[50], d[50];
ll ans = 0;
int A[10];
void dfs(int start, int end, int siz, int pos);

int main() {
	cin >> N >> M >> Q;
	for (int i = 0; i < Q; i++) {
		cin >> a[i] >> b[i] >> c[i] >> d[i];
	}
	dfs(1, M+1, N, 0);
	cout << ans << "\n";
	return 0;
}

void dfs(int start, int end, int siz, int pos) {
	if (pos == siz) {
		ll point = 0;
		for (int i = 0; i < Q; i++) {
			if (A[b[i] - 1] - A[a[i] - 1] == c[i]) {
				point += d[i];
			}
		}
		ans = max(ans, point);
		return;
	}
	for (int i = start; i < end; i++) {
		A[pos] = i;
		dfs(i, end, siz, pos+1);
	}
}
