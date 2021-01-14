import math
from functools import reduce
from collections import deque
N=int(input())
z = [None] * N
w = [None] * N
for i in range(N):
	x,y = map(int,input().split())
	z[i],w[i] = x+y, x-y
print(max(max(z)-min(z),max(w)-min(w)))
# max(|xi-xj|+|yi-yj|)
# max((xi-xj)+(yi-yj),(xi-xj)-(yi-yj),-(xi-xj)+(yi-yj),-(xi-xj)-(yi-yj))
# max((xi+yi)-(xj+yj),(xi-yi)-(xj-yj),-(xi-yi)+(xj-yj),-(xi+yi)+(xj+yj))
# max(z[i]-z[j],w[i]-w[j],-w[i]+w[j],-z[i]+z[j])
# max(|z[i]-z[j]|,|w[i]-w[j]|)
# max(max(z)-min(z),max(w)-min(w))
