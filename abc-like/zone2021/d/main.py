from collections import deque

T = deque()
Trev = deque()
flipped = False
void = True
for c in input():
	if c == 'R':
		flipped = not flipped
	else:
		if flipped:
			if len(Trev) > 0 and Trev[-1] == c:
				Trev.pop()
			elif len(Trev) == 0 and len(T) > 0 and T[0] == c:
				T.popleft()
			else:
				Trev.append(c)
		else:
			if len(T) > 0 and T[-1] == c:
				T.pop()
			elif len(T) == 0 and len(Trev) > 0 and Trev[0] == c:
				Trev.popleft()
			else:
				T.append(c)
if flipped:
	print(''.join(reversed(T)), ''.join(Trev), sep='')
else:
	print(''.join(reversed(Trev)), ''.join(T), sep='')
