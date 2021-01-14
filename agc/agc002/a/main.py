import math
from functools import reduce
from collections import deque
a,b = map(int,input().split())
if a <= 0 <= b:
	print('Zero')
elif b < 0 and (b-a+1)%2==1:
	print('Negative')
else:
	print('Positive')
