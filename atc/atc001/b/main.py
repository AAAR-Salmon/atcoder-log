class UnionFind:
	def __init__(self, N):
		self.__size = N
		self.__parent = [-1] * N

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
		if -self.__parent[X] < -self.__parent[Y]:
			X,Y=Y,X
		self.__parent[X] += self.__parent[Y]
		self.__parent[Y] = X

N,Q=map(int,input().split())
G=UnionFind(N)
for _ in range(Q):
	P,A,B=map(int,input().split())
	if P == 0:
		G.union(A,B)
	else:
		print('Yes' if G.find(A) == G.find(B) else 'No')
