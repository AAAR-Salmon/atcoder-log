from functools import reduce
N=int(input())
L=list(map(int,input().split()))
sum=reduce(lambda a,b:a+b,L)
ok=True
for l in L:
  if l >= sum - l:
    ok=False
print('Yes' if ok else 'No')
