import math
from functools import reduce
from collections import deque
S = input()
ans = 'AC'
i = 0
if S[i] != 'A':
	ans = 'WA'

i += 1
Cappeared = False
while i < len(S):
	if not 97 <= ord(S[i]) <= 122:
		if not 2 <= i <= len(S) - 2:
			ans = 'WA'
			break
		elif Cappeared:
			ans = 'WA'
			break
		elif S[i] == 'C':
			Cappeared = True
		else:
			ans = "WA"
			break
	i += 1
if not Cappeared:
	ans = 'WA'
print(ans)
