from functools import reduce
N,A,B = map(int,input().split())
ans = 0
for i in range(1,N+1):
	sum = reduce(lambda l,r: l+int(r), str(i), 0)
	if A <= sum <= B:
		ans += i
print(ans)
