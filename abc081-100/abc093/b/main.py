import math
from functools import reduce
from collections import deque
A,B,K = map(int,input().split())
if A+K-1 < B-K+1:
	print(*range(A,A+K), sep='\n')
	print(*range(B-K+1,B+1), sep='\n')
else:
	print(*range(A,B+1), sep='\n')
