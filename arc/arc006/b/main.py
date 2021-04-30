N,L = map(int,input().split())
grid = [input() for _ in range(L+1)]
pos = grid[L].index('o')
for i in range(L - 1, -1, -1):
	if pos >= 2 and grid[i][pos - 1] == '-':
		pos -= 2
	elif pos <= N * 2 - 4 and grid[i][pos + 1] == '-':
		pos += 2
print(pos // 2 + 1)
