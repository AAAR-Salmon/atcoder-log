from collections import deque
H,W = map(int,input().split())
grid = [None] * H
telep = [[] for _ in range(26)]
for i in range(H):
	grid[i] = input()
	for j in range(W):
		if grid[i][j] == 'S':
			x,y=i,j
		elif grid[i][j].islower():
			telep[ord(grid[i][j]) - 97].append((i,j))

visited=[[-1] * W for _ in range(H)]
visited[x][y] = 0
q = deque([(x,y)])
while q:
	x,y = q.popleft()
	if grid[x][y].islower():
		for (i,j) in telep[ord(grid[x][y]) - 97]:
			if visited[i][j] == -1:
				visited[i][j] = visited[x][y] + 1
				q.append((i,j))
		telep[ord(grid[x][y]) - 97].clear()
	for (i,j) in [(x+1,y), (x,y+1), (x-1,y), (x,y-1)]:
		if not (0 <= i < H and 0 <= j < W) or grid[i][j] == '#':
			continue
		if grid[i][j] == 'G':
			print(visited[x][y] + 1)
			exit(0)
		if visited[i][j] == -1:
			visited[i][j] = visited[x][y] + 1
			q.append((i,j))
print(-1)
