import math
from functools import reduce
from collections import deque
N = int(input())
D,X = map(int,input().split())
A = [int(input()) for _ in range(N)]
ans = X
for a in A:
	ans += (D+a-1) // a
print(ans)
