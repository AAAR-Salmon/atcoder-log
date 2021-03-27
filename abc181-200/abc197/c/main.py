from functools import reduce
from operator import xor, or_

N = int(input())
A = list(map(int,input().split()))

ans = reduce(or_, A)

# i番目とi+1番目の間を区切るならばi番目のビットは1
for b in range(1 << N - 1):
	groups = []
	g = A[0]
	for i in range(1, N):
		if b >> (i - 1) & 1:
			groups.append(g)
			g = A[i]
		else:
			g |= A[i]
	groups.append(g)
	ans = min(ans, reduce(xor, groups))
print(ans)
