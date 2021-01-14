import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

def main():
	N,Q = map(int,input().split())
	A = list(map(int,input().split()))
	st = Segtree(lambda x,y:x^y, A)
	for i in range(Q):
		T,X,Y = map(int,input().split())
		if T == 1:
			st.set(X-1, st.get(X-1) ^ Y)
		else:
			print(st.find(X-1,Y))

class Segtree():
	def __init__(self, function, iterable, identity = 0):
		l = len(iterable)
		assert(l > 0)
		self.__fn = function
		self.__identity = identity
		depth = 0
		while 1 << depth <= l:
			depth += 1
		self.__depth = depth
		self.__bin = [identity] * ((1 << self.__depth + 1) - 1)
		self.__leaves = 1 << self.__depth
		self.__offset = self.__leaves - 1
		for i in range(l):
			self.__bin[self.__offset + i] = iterable[i]
		for i in range(self.__offset - 1, -1, -1):
			self.__bin[i] = self.__fn(
				self.__bin[2 * i + 1],
				self.__bin[2 * i + 2]
			)

	def set(self, i, x):
		i = self.__offset + i
		self.__bin[i] = x
		while i > 0:
			i = (i - 1) // 2
			self.__bin[i] = self.__fn(
				self.__bin[2 * i + 1],
				self.__bin[2 * i + 2]
			)

	def get(self, i):
		return self.__bin[self.__offset + i]

	def find(self, l, r):
		return self.__find(l, r, 0, 0, self.__leaves)

	def __find(self, l, r, node, i, j):
		assert(l < r and i < j)
		if r <= i or j <= l:
			return self.__identity
		elif l <= i and j <= r:
			return self.__bin[node]
		else:
			k = (i + j) // 2
			return self.__fn(
				self.__find(l, r, 2 * node + 1, i, k),
				self.__find(l, r, 2 * node + 2, k, j)
			)

main()
