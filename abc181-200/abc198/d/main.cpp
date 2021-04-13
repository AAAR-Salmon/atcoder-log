#include <iostream>
#include <set>
#include <map>
#include <regex>

using namespace std;

bool done[10] = { false };
map<char, char> map_of_chars;
string s1, s2, s3;

void dfs(map<char, char>::iterator it);

int main() {
	cin >> s1 >> s2 >> s3;
	set<char> set_of_chars;
	for (const auto &c : s1) {
		set_of_chars.insert(c);
	}
	for (const auto &c : s2) {
		set_of_chars.insert(c);
	}
	for (const auto &c : s3) {
		set_of_chars.insert(c);
	}

	if (set_of_chars.size() > 10) {
		cout << "UNSOLVABLE" << endl;
		return 0;
	}

	for (const auto &c : set_of_chars) {
		map_of_chars.emplace(c, 0);
	}

	dfs(map_of_chars.begin());
	cout << "UNSOLVABLE" << "\n";
	return 0;
}

void dfs(map<char, char>::iterator it) {
	if (it == map_of_chars.end()) {
		string n1 = s1;
		string n2 = s2;
		string n3 = s3;
		for (auto &c : n1) {
			c = map_of_chars[c];
		}
		for (auto &c : n2) {
			c = map_of_chars[c];
		}
		for (auto &c : n3) {
			c = map_of_chars[c];
		}
		if (stoll(n1) + stoll(n2) == stoll(n3)) {
			cout << n1 << "\n";
			cout << n2 << "\n";
			cout << n3 << "\n";
			exit(0);
		}
		return;
	}
	int is_continued = 1;
	char is_first_char =
		it->first == s1[0] || it->first == s2[0] || it->first == s3[0];
	for (char i = is_first_char; i < 10 && is_continued; i++) {
		if (done[i]) {
			continue;
		}
		done[i] = true;
		it->second = '0' + i;
		dfs(next(it));
		done[i] = false;
	}
}
