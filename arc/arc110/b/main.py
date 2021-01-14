import math
from functools import reduce
from collections import deque
N = int(input())
T = input()
if '00' in T or '010' in T or '111' in T:
	print(0)
else:
	if N >= 3:
		ts = T[0:3]
		te = T[-3:]
		if ts == '101':
			N += 1
		elif ts == '011':
			N += 2
		if te == '101':
			N += 2
		elif te == '011':
			N += 1
		print(10**10 - N // 3 + 1)
	elif N == 2:
		if T == '01':
			print(10**10-1)
		else:
			print(10**10)
	else:
		if T == '1':
			print(2*10**10)
		else:
			print(10**10)
