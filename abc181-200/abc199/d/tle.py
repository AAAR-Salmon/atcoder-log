import sys
sys.setrecursionlimit(1000000)

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

  def group(self, i):
    return [j for j in range(self.__size) if self.same(i, j)]

  def count_group(self):
    return len(self.roots())


N,M = map(int,input().split())
edges = [[] for _ in range(N)]
color = [None] * N
uf = UnionFind(N)
for _ in range(M):
	A,B = map(lambda x:int(x)-1,input().split())
	uf.union(A,B)
	edges[A].append(B)
	edges[B].append(A)

def dfs(i, size):
	if i == size:
		return 1
	res = 0
	v = g[i]
	for c in range(3):
		if any(c == color[u] for u in edges[v]):
			continue
		color[v] = c
		res += dfs(i+1, size)
		color[v] = None
	return res

ans = 1
for r in uf.roots():
	g = uf.group(r)
	color[g[0]] = 0
	cnt = dfs(1, uf.size(r))
	ans *= cnt * 3
	if cnt == 0:
		break

print(ans)
