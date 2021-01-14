import math
from functools import reduce
from collections import deque
N = int(input())
A = sorted(map(int,input().split()))
lim = max(A)
dp = [True] * (lim+1)
p = 0
for a in A:
	if a == p:
		dp[a] = False
		continue
	i = 2
	while a * i <= lim:
		dp[a * i] = False
		i += 1
	p = a
ans = 0
for a in A:
	ans += dp[a] == True
print(ans)
