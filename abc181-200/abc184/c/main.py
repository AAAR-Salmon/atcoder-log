import math
from functools import reduce
from collections import deque
r1,c1=map(int,input().split())
r2,c2=map(int,input().split())
dr,dc=r2-r1,c2-c1
if (dr,dc) == (0,0):
	print(0)
elif dr+dc == 0 or dr-dc == 0 or abs(dr)+abs(dc) <= 3:
	print(1)
elif (dr+dc)%2 == 0 or abs(dr+dc) <= 4 or abs(dr-dc) <= 4 or abs(dr)+abs(dc) <= 6:
	print(2)
else:
	print(3)
