import math
import functools
N=int(input())
a=list(map(int,input().split()))
print(functools.reduce(math.gcd, a))
