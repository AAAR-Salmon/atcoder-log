import math
from functools import reduce
from collections import deque
N,W = map(int,input().split())
imos = [0] * 200001
T_max = 0
for _ in range(N):
	S,T,P = map(int,input().split())
	imos[S] += P
	imos[T] -= P
	T_max = max(T_max, T)
ans = 'Yes'
w = 0
for i in range(T_max):
	w += imos[i]
	if w > W:
		ans = 'No'
		break
print(ans)
