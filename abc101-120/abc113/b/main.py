import math
from functools import reduce
from collections import deque
N=int(input())
T,A=map(int,input().split())
H=list(map(int,input().split()))
ans={'index':0, 'error':abs(T-H[0]*0.006-A)}
for i in range(1,N):
	if abs(T-H[i]*0.006-A) < ans['error']:
		ans={'index':i, 'error':abs(T-H[i]*0.006-A)}
print(ans['index']+1)
