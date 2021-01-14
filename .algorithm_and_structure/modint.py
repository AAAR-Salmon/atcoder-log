class Modint:
	def __init__(self, value, mod):
		self.__mod = mod
		self.__val = value % mod

	def __repr__(self):
		return f'<Modint object __mod = {self.__mod} at {hex(id(self))}>'

	def __str__(self):
		return str(self.__val)

	def get(self):
		return self.__val

	def __eq__(self, other):
		return self.__val == other % self.__mod

	def __ne__(self, other):
		return self.__val != other % self.__mod

	def __add__(self, other):
		return self.__class__(self.__val + other, self.__mod)

	def __sub__(self, other):
		return self.__class__(self.__val - other, self.__mod)

	def __mul__(self, other):
		return self.__class__(self.__val * other, self.__mod)

	def __pow__(self, other):
		if other == 0:
			return self.__class__(1, self.__mod)
		elif 0 < other < self.__mod - 1:
			if other % 2 == 0:
				return (self * self.__val) ** (other // 2)
			else:
				return self ** (other - 1) * self.__val
		else:
			return self ** (other % (self.__mod - 1))

	def __floordiv__(self, other):
		return self.__class__(other, self.__mod) ** (self.__mod - 2) * self.__val

	def __iadd__(self, other):
		self.__val = (self.__val + other) % self.__mod
		return self

	def __isub__(self, other):
		self.__val = (self.__val - other) % self.__mod
		return self

	def __imul__(self, other):
		self.__val = (self.__val * other) % self.__mod
		return self

	def __ipow__(self, other):
		if other == 0:
			self.__val = 1
			return self
		elif 0 < other < self.__mod - 1:
			if other % 2 == 0:
				self.__val = self.__val ** 2 % self.__mod
				self **= other // 2
				return self
			else:
				v = self.__val
				self **= other - 1
				self *= v
				return self
		else:
			self **= other % (self.__mod - 1)
			return self

	def __ifloordiv__(self, other):
		inv_other = self.__class__(other, self.__mod)
		inv_other **= self.__mod - 2
		self.__val = self.__val * inv_other.get() % self.__mod
		return self

	def __neg__(self):
		return self.__class__(-self.__val, self.__mod)

	def __pos__(self):
		return self.__class__(self.__val, self.__mod)
