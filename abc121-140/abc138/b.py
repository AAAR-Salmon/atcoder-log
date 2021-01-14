from functools import reduce
N=int(input())
A=list(map(int,input().split()))
h=reduce(lambda a,b:a+1/b, A, 0)
print(1/h)
