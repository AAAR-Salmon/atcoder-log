from math import gcd
from functools import reduce

N,X = map(int,input().split())
x = list(map(lambda x:abs(int(x)-X),input().split()))
print(reduce(gcd, x))
