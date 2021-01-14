#include <bits/stdc++.h>
using namespace std;
#define rep(i,r) for (int i = 0; i < r; i++)
#define repeq(i,r) for (int i = 0; i <= r; i++)
#define isc(n) scanf("%d", &n)

int main() {
  int N; isc(N);
  string res = "No";
  if (N / 100 == 7) res = "Yes";
  if (N % 100 / 10 == 7) res = "Yes";
  if (N % 10 == 7) res = "Yes";
  cout << res << endl;
  return 0;
}
