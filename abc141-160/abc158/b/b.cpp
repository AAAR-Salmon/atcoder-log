#include <bits/stdc++.h>
using namespace std;
#define rep(i,r) for (int i = 0; i < r; i++)
#define repeq(i,r) for (int i = 0; i <= r; i++)

int main() {
  long N;
  long A, B;
  cin >> N >> A >> B;
  long loop = A + B;
  long surplus;

  cout << (N / loop * A + ((surplus = N % loop) > A ? A : surplus)) << endl;
  return 0;
}
