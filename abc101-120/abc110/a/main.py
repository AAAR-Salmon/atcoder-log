import math
from functools import reduce
from collections import deque
A,B,C=list(map(int,input().split()))
ans=max(A*10+B+C,A+B*10+C,A+B+C*10)
print(ans)
