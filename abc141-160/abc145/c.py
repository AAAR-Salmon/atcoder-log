import math
N=int(input())
x=[0]*N
y=[0]*N
for i in range(N):
  x[i],y[i]=map(int,input().split())
ans=0
for i in range(N-1):
  for j in range(i+1,N):
    ans+=math.sqrt((x[i]-x[j])**2+(y[i]-y[j])**2)
print(ans*2/N)
