import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

N = int(input())
x,y = ([None] * N for _ in range(2))
for i in range(N):
    x[i],y[i] = map(int,input().split())
ans = 0
for i in range(N):
    for j in range(i):
        if abs(y[i] - y[j]) <= abs(x[i] - x[j]):
            ans += 1
print(ans)