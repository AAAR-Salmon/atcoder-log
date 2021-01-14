import math
from functools import reduce
from collections import deque
N = int(input())
S = input()
R,G,B = 0,0,0
for i in range(N):
	if S[i] == 'R':
		R += 1
	elif S[i] == 'G':
		G += 1
	elif S[i] == 'B':
		B += 1
ans = R*G*B
for i in range(0,N-2):
	for j in range(i+1,N-1):
		k = 2*j-i
		if k < N and (S[i] != S[j] and S[j] != S[k] and S[k] != S[i]):
			ans -= 1
print(ans)
