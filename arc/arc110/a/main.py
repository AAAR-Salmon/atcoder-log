import math
from functools import reduce
from collections import deque
N = int(input())
ans = 1
for i in range(N,1,-1):
	ans = ans*i//math.gcd(ans, i)
print(ans + 1)
