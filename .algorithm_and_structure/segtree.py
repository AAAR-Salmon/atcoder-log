class Segtree():
	def __init__(self, v, op, e):
		self.__op = op
		self.__e = e
		self.__n = len(v)
		log = 0
		while 1 << log < self.__n:
			log += 1
		self.__log = log
		self.__size = 1 << log
		self.__d = [e] * (2 * self.__size)
		for i in range(self.__n):
			self.__d[self.__size + i] = v[i]
		for i in range(self.__size - 1, 0, -1):
			self.__update(i)

	def __update(self, k):
		self.__d[k] = self.__op(self.__d[2 * k], self.__d[2 * k + 1])

	def set(self, p, x):
		assert(0 <= p < self.__n)
		p += self.__size
		self.__d[p] = x
		for i in range(1, self.__log + 1):
			self.__update(p >> i)

	def get(self, p):
		assert(0 <= p < self.__n)
		return self.__d[p + self.__size]

	def prod(self, l, r):
		assert(0 <= l <= r <= self.__n)
		sml = self.__e
		smr = self.__e
		l += self.__size
		r += self.__size

		while l < r:
			if l & 1:
				sml = self.__op(sml, self.__d[l])
				l += 1
			if r & 1:
				smr = self.__op(self.__d[r], smr)
				r += 1
			l >>= 1
			r >>= 1
		return self.__op(sml, smr)

	def all_prod(self):
		return self.__d[1]
