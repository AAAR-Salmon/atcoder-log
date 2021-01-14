import math
N=int(input())
for i in range(math.ceil(math.sqrt(N)), 0, -1):
  if N % i == 0:
    print((i - 1) + (N // i - 1))
    break
