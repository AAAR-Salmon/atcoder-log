import math
from functools import reduce
from collections import deque
A,B,X = map(int,input().split())
print('YES' if A <= X <= A+B else 'NO')
