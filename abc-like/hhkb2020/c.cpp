#include <iostream>
#include <vector>
#include <set>
using namespace std;
using ll = long long;

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);

	int N;
	cin >> N;
	set<int> s{};
	for (int i = 0; i <= 200000; i++) {
		s.insert(s.end(), i);
	}
	for (int i = 0; i < N; i++) {
		int p;
		cin >> p;
		if (s.find(p) != s.end()) {
			s.erase(p);
		}
		cout << *s.begin() << "\n";
	}

	return 0;
}
