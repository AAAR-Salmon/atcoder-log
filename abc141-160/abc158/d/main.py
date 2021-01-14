from collections import deque
S = deque(input())
Q = int(input())
r = False
for _ in range(Q):
	Query = list(input().split())
	if Query[0] == '1':
		r = not r
	else:
		if (Query[1] == '1') is not r:
			S.appendleft(Query[2])
		else:
			S.append(Query[2])
print(''.join(reversed(S) if r else S))
