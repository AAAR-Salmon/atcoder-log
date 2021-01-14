import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

def main():
	N,M,K = map(int,input().split())
	chainFriend = UnionFind(N)
	ans = [-1] * N
	for _ in range(M):
		A,B = map(intm1,input().split())
		chainFriend.union(A,B)
		ans[A] -= 1
		ans[B] -= 1
	for i in range(N):
		ans[i] += chainFriend.size(i)
	for _ in range(K):
		C,D = map(intm1,input().split())
		if chainFriend.same(C,D):
			ans[C] -= 1
			ans[D] -= 1
	print(*ans)

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
		x,y = self.find(i),self.find(j)
		if x == y:
			return x
		elif -self.__parent[x] < -self.__parent[y]:
			x,y = y,x
		self.__parent[x] += self.__parent[y]
		self.__parent[y] = x
		return x

	def same(self, i, j):
		assert 0 <= i < self.__size
		assert 0 <= j < self.__size
		return self.find(i) == self.find(j)

	def size(self, i):
		assert 0 <= i < self.__size
		return -self.__parent[self.find(i)]

	def roots(self):
		return [i for i,x in enumerate(self.__parent) if x < 0]

	def count_group(self):
		return len(self.roots())

main()
