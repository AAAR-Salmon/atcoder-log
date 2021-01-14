#include <bits/stdc++.h>
using namespace std;
#define rep(i,r) for (int i = 0; i < r; i++)
#define repeq(i,r) for (int i = 0; i <= r; i++)

int main() {
  int N, M;
  cin >> N >> M;
  int A[N];
  rep(i,N) cin >> A[i];
  float sum = 0;
  rep(i,N) sum += A[i];

  int selectable = 0;
  rep(i,N) {
    if (A[i] >= sum / M / 4) selectable++;
  }
  cout << (selectable >= M ? "Yes" : "No") << endl;
  return 0;
}
