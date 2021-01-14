class UnionFind:
	def __init__(self, n):
		self.__size = n
		self.__parent = [-1] * n

	def find(self, x):
		assert 0 <= x < self.__size
		if self.__parent[x] < 0:
			return x
		else:
			self.__parent[x] = self.find(self.__parent[x])
			return self.__parent[x]

	def union(self, x, y):
		assert 0 <= x < self.__size
		assert 0 <= y < self.__size
		X = self.find(x)
		Y = self.find(y)
		if X == Y:
			return
		elif -self.__parent[X] < -self.__parent[Y]:
			X,Y=Y,X
		self.__parent[X] += self.__parent[Y]
		self.__parent[Y] = X

	def same(self, x, y):
		assert 0 <= x < self.__size
		assert 0 <= y < self.__size
		return self.find(x) == self.find(y)

N,Q=map(int,input().split())
G=UnionFind(N)
for _ in range(Q):
	t,u,v=map(int,input().split())
	if t == 0:
		G.union(u,v)
	else:
		print(1 if G.same(u,v) else 0)
