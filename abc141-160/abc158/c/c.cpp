#include <bits/stdc++.h>
using namespace std;
#define rep(i,r) for (int i = 0; i < r; i++)
#define repeq(i,r) for (int i = 0; i <= r; i++)

int main() {
  int A, B;
  cin >> A >> B;
  for (int i = 1; i <= 1000; i++) {
    if (i * 8 / 100 == A && i * 10 / 100 == B) {
      cout << i << endl;
      return 0;
    }
  }
  cout << "-1" << endl;
  return 0;
}
