from collections import deque

T = deque()
flipped = False
void = True
for c in input():
	if c == 'R':
		flipped = not flipped
	else:
		if len(T) == 0:
			T.append(c)
		else:
			if flipped:
				if T[0] == c:
					T.popleft()
				else:
					T.appendleft(c)
			else:
				if T[-1] == c:
					T.pop()
				else:
					T.append(c)
print(''.join(reversed(T) if flipped else T))
