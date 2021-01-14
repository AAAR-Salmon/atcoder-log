x=[0]*11
r,D,x[0]=map(int,input().split())
for i in range(10):
  x[i+1] = r*x[i]-D
  print(x[i+1])
