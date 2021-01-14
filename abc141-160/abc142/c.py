N=int(input())
A=list(map(int,input().split()))
O=[0]*N
for i,a in enumerate(A):
  O[a - 1] = i + 1
print(*O)
