from functools import reduce
N=int(input())
v=list(map(int,input().split()))
v.sort()
print(reduce(lambda a,b:(a+b)/2,v))
