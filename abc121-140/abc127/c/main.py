N,M=map(int,input().split())
Lmax,Rmin=map(int,input().split())
for i in range(1,M):
  L,R=map(int,input().split())
  Lmax=max(Lmax,L)
  Rmin=min(Rmin,R)
if Lmax <= Rmin:
  print(Rmin - Lmax + 1)
else:
  print(0)
