MOD = 998244353

class UnionFind():
	def __init__(self, n):
		self.__size = n
		self.__parent = [-1] * n

	def find(self, i):
		assert 0 <= i < self.__size
		if self.__parent[i] < 0:
			return i
		else:
			self.__parent[i] = self.find(self.__parent[i])
			return self.__parent[i]

	def union(self, i, j):
		assert 0 <= i < self.__size
		assert 0 <= j < self.__size
		x, y = self.find(i), self.find(j)
		if x == y:
			return x
		elif -self.__parent[x] < -self.__parent[y]:
			x, y = y, x
		self.__parent[x] += self.__parent[y]
		self.__parent[y] = x
		return x

	def roots(self):
		return [i for i, x in enumerate(self.__parent) if x < 0]

	def count_group(self):
		return len(self.roots())

N = int(input())
F = UnionFind(N)
f = list(map(int,input().split()))
for i in range(N):
	F.union(i, f[i] - 1)
print((pow(2, F.count_group(), MOD) - 1) % MOD)
