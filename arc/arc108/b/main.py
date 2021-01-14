import math
from functools import reduce
from collections import deque
N=int(input())
s=input()
i=0
while i < len(s):
	if s[i:i+3] == 'fox':
		s = s[:i] + s[i+3:]
		i -= 2
	else:
		i += 1
print(len(s))
