import math
from functools import reduce
from collections import deque
S,P = map(int,input().split())
ok=0
ng=P+1
while ng-ok>1:
	mid=(ok+ng)//2
	if mid**2<=P:
		ok=mid
	else:
		ng=mid
rtP=ok
ans='No'
for N in range(1,rtP+1):
	if P % N == 0 and N + P // N == S:
		ans='Yes'
		break
print(ans)
