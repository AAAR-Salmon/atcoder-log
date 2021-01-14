import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

L,R = map(int,input().split())
ans = 2018
for i in range(L,min(L+2019,R+1)):
	for j in range(i+1,min(L+2019,R+1)):
		if i * j % 2019 < ans:
			ans = i * j % 2019
print(ans)
