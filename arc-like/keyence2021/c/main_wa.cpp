#include <iostream>
using namespace std;
using ll = long long;
ll const MOD = 998244353;

char c[5001][5001];
ll dp[5001][5001];
int dot_left[5001][5001];
int dot_up[5001][5001];

ll modpow(ll a, ll p, ll d) {
  if (p == 0) {
    return 1;
  } else if (p == 1) {
    return a % d;
  } else if (p % 2 == 0) {
    return modpow(a * 2 % d, p / 2, d);
  } else {
    return modpow(a, p - 1, d) * a % d;
  }
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int H, W, K;
  cin >> H >> W >> K;
  for (int i = 0; i < K; i++) {
    int h, w;
    cin >> h >> w;
    cin >> c[h][w];
    dot_left[h][w] = 1;
    dot_up[h][w] = 1;
  }

  for (int i = 1; i <= H; i++) {
    for (int j = 1; j <= W; j++) {
      dot_left[i][j] += dot_left[i][j - 1];
      dot_up[i][j] += dot_up[i - 1][j];
    }
  }
  for (int i = 1; i <= H; i++) {
    for (int j = 1; j <= W; j++) {
      dot_left[i][j] = j - dot_left[i][j];
      dot_up[i][j] = i - dot_up[i][j];
    }
  }

  for (int j = 0; j <= W; j++) {
    c[0][j] = 'R';
  }
  for (int i = 0; i <= H; i++) {
    c[i][0] = 'D';
  }
  dp[1][1] = 1;

  for (int i = 1; i <= H; i++) {
    for (int j = 1; j <= W; j++) {
      if (c[i - 1][j] != 'R') {
        dp[i][j] += dp[i - 1][j] * (c[i - 1][j] == '.' ? 2 : 1) *
                    modpow(3, dot_left[i - 1][W] - dot_left[i - 1][j], MOD);
      }
      if (c[i][j - 1] != 'D') {
        dp[i][j] += dp[i][j - 1] * (c[i][j - 1] == '.' ? 2 : 1) *
                    modpow(3, dot_up[H][j - 1] - dot_left[i][j - 1], MOD);
      }
      dp[i][j] %= MOD;
    }
  }

  cout << dp[H][W] << "\n";
  return 0;
}
