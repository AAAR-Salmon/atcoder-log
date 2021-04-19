from functools import reduce

N = int(input())
A = sorted(map(int,input().split()))
print(reduce(
	lambda x,y: x * y % 1000000007,
	(A[i] - A[i - 1] + 1 for i in range(1, N)),
	A[0] + 1
))
