import math
from functools import reduce
from collections import deque
N = int(input())
K = int(input())
X = list(map(int,input().split()))
ans = 0
for x in X:
	ans += min(x, K-x)
print(ans * 2)
