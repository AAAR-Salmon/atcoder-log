#include <bits/stdc++.h>
using namespace std;
#define rep(i,r) for (int i = 0; i < r; i++)
#define repeq(i,r) for (int i = 0; i <= r; i++)
#define isc(n) scanf("%d", &n)

int main() {
  int N; isc(N);
  long res = 0;
  for (int i = 1; i <= N; i++) {
    if (i % 3 != 0 && i % 5 != 0) res += i;
  }
  cout << res << endl;
  return 0;
}
