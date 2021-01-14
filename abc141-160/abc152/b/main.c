#include <stdio.h>
#define rep(i,r) for (int i = 0; i < r; i++)

long repunit(long unit, long digits) {
  return digits == 1 ? unit : repunit(unit, digits - 1) * 10 + unit;
}

int main() {
  long a, b;
  scanf("%ld%ld", &a, &b);
  printf("%ld", repunit(a < b ? a : b, a < b ? b : a));
  return 0;
}
