#include <algorithm>
#include <iostream>

using namespace std;

using ll = long long;
ll const MOD = 1000000007;

template <typename T>
void chmax(T &target, T num) {
  if (num > target) {
    target = num;
  }
}

ll dp[3005][3005][4] = {0LL};
ll value_grid[3005][3005] = {0LL};

int main() {
  int R, C, K;
  cin >> R >> C >> K;
  for (int i = 0; i < K; i++) {
    int r, c;
    ll v;
    cin >> r >> c >> v;
    value_grid[r][c] = v;
  }

  for (int i = 1; i <= R; i++) {
    for (int j = 1; j <= C; j++) {
      for (int k = 0; k <= 3; k++) {
        chmax(dp[i][j][0], dp[i - 1][j][k]);
        chmax(dp[i][j][1], dp[i - 1][j][k] + value_grid[i][j]);
        chmax(dp[i][j][k], dp[i][j - 1][k]);
      }
      for (int k = 1; k <= 3; k++) {
        chmax(dp[i][j][k], dp[i][j - 1][k - 1] + value_grid[i][j]);
      }
    }
  }

  cout << max({dp[R][C][0], dp[R][C][1], dp[R][C][2], dp[R][C][3]}) << "\n";

  return 0;
}
