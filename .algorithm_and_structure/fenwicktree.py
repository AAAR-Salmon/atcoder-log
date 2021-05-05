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
