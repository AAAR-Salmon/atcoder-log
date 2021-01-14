from functools import reduce

N = int(input())
a = list(map(int,input().split()))
allxor = reduce(lambda x,y:x^y, a)
print(*map(lambda x:x^allxor, a))
