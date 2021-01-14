import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

N,K = map(int,input().split())
P = list(map(intm1,input().split()))
C = list(map(int,input().split()))

# 最初にコマを置くマスに0を選んだときの累積スコア
p = 0
score = [0] * (N+1)
for i in range(N):
	p = P[p]
	score[i+1] = score[i] + C[p]
