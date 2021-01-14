import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

N = int(input())
yukensha = [None] * N
for i in range(N):
    yukensha[i] = list(map(int, input().split()))
ans = 0
tak = 0
aoki = sum(map(lambda x: x[0], yukensha))
yukensha.sort(reverse=True, key=lambda x: x[0]*2+x[1])
while tak <= aoki:
    tak += yukensha[ans][0] * 2 + yukensha[ans][1]
    ans += 1
print(ans)