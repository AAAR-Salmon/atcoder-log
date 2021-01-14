import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]
known_worst = max(AB, key=lambda x: x[0])
print(known_worst[0] + known_worst[1])
