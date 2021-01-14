import math
from functools import reduce
from collections import deque
int1 = lambda x:int(x)-1
N,M = map(int,input().split())
for i in range(M):
	u,v,c = map(int,input().split())
	u -= 1
	v -= 1
