from functools import reduce
from collections import deque
N=int(input())
c=input()
cnt=ans=0
for ci in c:
	if ci == 'R':
		cnt += 1
for ci in c[cnt:]:
	if ci == 'R':
		ans += 1
print(ans)
