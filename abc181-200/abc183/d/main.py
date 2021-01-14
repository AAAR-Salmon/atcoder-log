import math
from functools import reduce
from collections import deque
N,W=map(int,input().split())
People=[None]*N
for i in range(N):
	S,T,P=map(int,input().split())
	People[i]={'S':S,'T':T,'P':P}
S=sorted(People, key=lambda p:p['S'])
T=sorted(People, key=lambda p:p['T'])
cap=0
s=t=0
ok=True
while s < N:
	if S[s]['S'] >= T[t]['T']:
		cap -= T[t]['P']
		t += 1
	else:
		cap += S[s]['P']
		s += 1
		if cap > W:
			ok=False
			break
print('Yes' if ok else 'No')
