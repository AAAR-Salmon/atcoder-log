#include <stdio.h>

int main() {
  int N;
  scanf("%d", &N);
  int count = 0;
  for (int i = 0, m = N, P; i < N; i++) {
    scanf("%d", &P);
    if (P <= m) {
      m = P;
      count++;
    }
  }
  printf("%d", count);
  return 0;
}
