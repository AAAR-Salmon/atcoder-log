#include <iostream>
#include <vector>
using namespace std;
using ll = long long;

ll pow(ll base, int ex) {
	if (ex == 0) {
		return 1;
	} else {
		return base * pow(base, ex - 1);
	}
}

int main() {
	ll N;
	cin >> N;
	N--;
	int nl = 1;
	while (N >= pow(26, nl)) {
		N -= pow(26, nl);
		nl++;
	}
	vector<char> name(nl, 'a');
	for (int i = nl - 1; N > 0; i--) {
		name.at(i) = (char) ('a' + N % 26);
		N /= 26;
	}
	for (auto c : name) {
		cout << c;
	}
	cout << endl;
	return 0;
}
