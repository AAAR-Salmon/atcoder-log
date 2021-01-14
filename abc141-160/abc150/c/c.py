N=int(input())
P=list(map(int,input().split()))
Q=list(map(int,input().split()))
seq=list(range(1,N+1))
done=[False]*N
perm=[0]*N

def DFS(func, pos, depth):
  if pos == depth:
    func()
    return
  for i in range(depth):
    if not done[i]:
      perm[pos] = seq[i]
      done[i] = True
      DFS(func, pos + 1, depth)
      done[i] = False

class count_order:
  def __init__(self, arr):
    self.cnt=0
    self.res=-1
    self.arr=arr

  def do(self):
    if self.arr == perm:
      self.res = self.cnt
    self.cnt += 1

A=count_order(P)
B=count_order(Q)
DFS(A.do, 0, N)
DFS(B.do, 0, N)
print(abs(A.res - B.res))
