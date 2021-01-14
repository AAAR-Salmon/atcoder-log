import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

A,B,C,D = map(int,input().split())
ans = B-A+1
ans -= B//C-(A+C-1)//C+1
ans -= B//D-(A+D-1)//D+1
E = C*D//math.gcd(C,D)
ans += B//E-(A+E-1)//E+1
print(ans)
