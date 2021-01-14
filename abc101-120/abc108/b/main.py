import math
from functools import reduce
from collections import deque
x1,y1,x2,y2 = map(int,input().split())
v12 = [x2-x1, y2-y1]
v23 = [-v12[1], v12[0]]
v34 = [-v23[1], v23[0]]
print(x2+v23[0], y2+v23[1], x2+v23[0]+v34[0], y2+v23[1]+v34[1])
