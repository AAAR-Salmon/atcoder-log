import math
from functools import reduce
from collections import deque
N,K=map(int,input().split())
h=[int(input()) for _ in range(N)]
h.sort()
dif_h=[h[i+K-1] - h[i] for i in range(N-K+1)]
print(min(dif_h))
