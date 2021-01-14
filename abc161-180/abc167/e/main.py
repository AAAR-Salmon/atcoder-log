import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

MOD = 998244353

N,M,K = map(int,input().split())

comb = [1] * (K + 1)
for i in range(1, K + 1):
    comb[i] = comb[i - 1] * (N - i) * pow(i, -1, MOD) % MOD

if M == 1:
    print(1 if K == N - 1 else 0)
    exit(0)
ans = 0
for i in range(K + 1):
    ans = (ans + comb[i] * M * pow(M - 1, N - 1 - i, MOD)) % MOD
print(ans)
