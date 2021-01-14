import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

S = input()
K = int(input())
firstNonOne = 0
for i in range(len(S)):
	if S[i] != '1':
		firstNonOne = i
		break
if firstNonOne <= K-1:
	print(S[firstNonOne])
else:
	print(1)
