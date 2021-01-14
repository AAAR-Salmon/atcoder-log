#include <iostream>
int main() {
  long N, K;
  std::cin >> N >> K;
  std::cout << (N % K * 2 < K ? N % K : K - N % K) << std::endl;
}
