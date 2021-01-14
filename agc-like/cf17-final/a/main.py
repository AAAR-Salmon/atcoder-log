import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

S = input()

def subAkihabara(bits):
	result = ''
	if bits & 1 << 0:
		result += 'A'
	result += 'KIH'
	if bits & 1 << 1:
		result += 'A'
	result += 'B'
	if bits & 1 << 2:
		result += 'A'
	result += 'R'
	if bits & 1 << 3:
		result += 'A'
	return result

for i in range(1 << 4):
	if S == subAkihabara(i):
		print('YES')
		exit(0)
print('NO')
