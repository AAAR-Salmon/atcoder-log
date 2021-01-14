from functools import reduce
N=int(input())
s=[]
t=[]
for _ in range(N):
  a=input().split()
  s.append(a[0])
  t.append(int(a[1]))
X=input()
ans=0
for i,title in enumerate(s):
  ans += t[i]
  if title == X:
    break
print(reduce(lambda a,b:a+b, t) - ans)
