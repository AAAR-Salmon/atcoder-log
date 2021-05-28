def dfs(cnt, k):
	if cnt == 8:
		ans = list(bytearray(b'.' * 8) for _ in range(8))
		for x, y in pieces:
			ans[x][y] = 81
		print(*(s.decode() for s in ans), sep='\n')
		exit(0)
	for l in range(k, 64):
		i = l // 8
		j = l % 8
		if any(i == x or j == y or abs(i - x) == abs(j - y) for x, y in pieces):
			continue
		pieces.append((i, j))
		dfs(cnt + 1, l + 1)
		pieces.pop()


pieces = []
cnt = 0
for i in range(8):
	S = input()
	for j in range(8):
		if S[j] == 'Q':
			if any(i == x or j == y or abs(i - x) == abs(j - y) for x, y in pieces):
				print('No Answer')
				exit(0)
			pieces.append((i, j))
			cnt += 1

dfs(cnt, 0)
print('No Answer')
