#include <iostream>
#include <algorithm>
#include <string>
#include <cctype>
using namespace std;

void toupper(string &S) {
	for (auto &c : S) {
		c = toupper(c);
	}
}

int main() {
	string s, t, res;
	cin >> s >> t;
	if (s == t) {
		res = "same";
	} else {
		toupper(s);
		toupper(t);
		if (s == t) {
			res = "case-insensitive";
		} else {
			res = "different";
		}
	}
	cout << res << endl;
	return 0;
}
