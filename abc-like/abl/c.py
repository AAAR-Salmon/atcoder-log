class UnionFind():
  def __init__(self, n):
    self.n = n
    self.parent = [-1] * n

  def find(self, i):
    assert 0 <= i < self.n
    if self.parent[i] < 0:
      return i
    else:
      self.parent[i] = self.find(self.parent[i])
      return self.parent[i]

  def union(self, i, j):
    assert 0 <= i < self.n
    assert 0 <= j < self.n
    x,y = self.find(i),self.find(j)
    if x == y:
      return x
    elif -self.parent[x] < -self.parent[y]:
      x,y = y,x
    self.parent[x] += self.parent[y]
    self.parent[y] = x
    return x

  def same(self, i, j):
    assert 0 <= i < self.n
    assert 0 <= j < self.n
    return self.find(i) == self.find(j)

  def size(self, i):
    assert 0 <= i < self.n
    return -self.parent[self.find(i)]

  def roots(self):
    return [i for i,x in enumerate(self.parent) if x < 0]

  def group_count(self):
    return len(self.roots())


N,M=map(int,input().split())
cities=UnionFind(N)
for _ in range(M):
  a,b=map(lambda n:int(n)-1,input().split())
  cities.union(a,b)
print(cities.group_count() - 1)
