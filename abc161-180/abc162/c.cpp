#include <stdio.h>
using namespace std;
#define repeq(i,r) for (int i = 1; i <= r; i++)
#define isc(n) scanf("%d", &n)

int gcd(int a, int b) {
  return a % b == 0 ? b : gcd(b, a % b);
}

int main() {
  int K; isc(K);
  long res = 0;
  repeq(i,K) repeq(j,K) repeq(k,K) res += gcd(gcd(i,j),k);
  printf("%ld", res);
  return 0;
}
