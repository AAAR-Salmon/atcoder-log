import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

N = int(input())
a,b = ([None] * (N) for _ in range(2))
children = [[] for _ in range(N + 1)]
parent = [None] * (N + 1)
for i in range(1, N):
    a[i],b[i] = map(int,input().split())
    children[a[i]].append(b[i])
    children[b[i]].append(a[i])

children[1].append(0)
q = deque([(1, 0)])
while q:
    n, p = q.popleft()
    parent[n] = p
    children[n].remove(p)
    for c in children[n]:
        q.append((c, n))

imos = [0] * (N + 1)

Q = int(input())
for i in range(Q):
    t,e,x = map(int,input().split())
    A,B = a[e],b[e]
    if t == 2:
        A,B = B,A
    if parent[A] == B:
        imos[A] += x
    else:
        imos[1] += x
        imos[B] -= x

q = deque([1])
while q:
    n = q.popleft()
    imos[n] += imos[parent[n]]
    q.extend(children[n])

for i in range(1, N + 1):
    print(imos[i])
