#include <iostream>
#include <map>
using namespace std;
using ll = long long;

int main() {
	int N;
	cin >> N;
	map<int, ll> A;
	for (int i = 0; i < N; i++) {
		int a;
		cin >> a;
		auto it = A.find(a);
		if (it == A.end()) {
			A.emplace(a, 1);
		} else {
			(it->second)++;
		}
	}
	ll S = 0;
	for (auto p : A) {
		S += p.first * p.second;
	}
	int Q;
	cin >> Q;
	for (int i = 0; i < Q; i++) {
		int B, C;
		cin >> B >> C;
		if (A.find(B) != A.end()) {
			S += (C - B) * A.at(B);
			if (A.find(C) == A.end()) {
				A.emplace(C, A.at(B));
			} else {
				A.at(C) += A.at(B);
			}
			A.erase(B);
		}
		cout << S << endl;
	}
	return 0;
}
