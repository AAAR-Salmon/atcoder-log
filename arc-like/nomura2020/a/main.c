#include <stdio.h>

int main() {
  int H1, M1, H2, M2, K;
  scanf("%d%d%d%d%d", &H1, &M1, &H2, &M2, &K);
  int l = H2 * 60 + M2 - H1 * 60 - M1 - K;
  printf("%d\n", l);
  return 0;
}
