class FenwickTree():
	def __init__(self, n):
		self.__n = n
		self.__data = [0] * n

	def add(self, i, x):
		while i < self.__n:
			self.__data[i] += x
			i |= ~i & -~i

	def sum(self, i):
		res = 0
		while i > 0:
			res += self.__data[i - 1]
			i ^= i & -i
		return res

N = int(input())
A = list(map(int,input().split()))
ft = FenwickTree(N)
inv = 0
for i in range(N):
	inv += i - ft.sum(A[i])
	ft.add(A[i], 1)
for a in A:
	print(inv)
	inv += N - 1 - a * 2
