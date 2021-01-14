from collections import deque
R,C=map(int,input().split())
y,x=map(lambda s:int(s)-1,input().split())
gy,gx=map(lambda s:int(s)-1,input().split())
c=[input() for _ in range(R)]
moves=[[0] * C for _ in range(R)]
q=deque([(y,x)])
while len(q) > 0:
	(y,x) = q.popleft()
	for (j,i) in [(y,x+1), (y,x-1), (y+1,x), (y-1,x)]:
		if (j,i) < (0,0) or (R,C) <= (j,i):
			continue
		if moves[j][i] > 0:
			continue
		if c[j][i] == '#':
			continue
		q.append((j,i))
		moves[j][i] = moves[y][x] + 1
		if (j,i) == (gy,gx):
			print(moves[j][i])
			exit()
