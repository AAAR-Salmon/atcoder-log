import math
from functools import reduce
from collections import deque
A,B,C,D = (int(input()) for _ in range(4))
print(min(A,B) + min(C,D))
