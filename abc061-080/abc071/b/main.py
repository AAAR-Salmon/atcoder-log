import math
from functools import reduce
from collections import deque
S = input()
unappeared = set(chr(ord('a')+i) for i in range(26))
for c in S:
	unappeared.discard(c)
if unappeared:
	for c in (chr(ord('a')+i) for i in range(26)):
		if c in unappeared:
			print(c)
			break
else:
	print('None')
