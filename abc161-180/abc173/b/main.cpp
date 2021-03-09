#include <iostream>
#include <string>
#include <map>
using namespace std;

int main() {
	int N;
	scanf("%d", &N);
	map<string, int> judge;
	for (int i = 0; i < N; i++) {
		string s;
		cin >> s;
		judge[s]++;
	}
	cout << "AC x " << judge["AC"] << endl;
	cout << "WA x " << judge["WA"] << endl;
	cout << "TLE x " << judge["TLE"] << endl;
	cout << "RE x " << judge["RE"] << endl;
	return 0;
}
