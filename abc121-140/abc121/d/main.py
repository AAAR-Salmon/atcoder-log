from functools import reduce
from operator import xor


def f(n):
	return reduce(xor, range(n // 4 * 4, n + 1))


A, B = map(int, input().split())
print(f(A - 1) ^ f(B))
