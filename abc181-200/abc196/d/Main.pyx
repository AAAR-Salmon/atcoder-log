cdef int H, W, A, B

H, W, A, B = map(int,input().split())

filled = [[False] * W for _ in range(H)]

cdef long long dfs(int h, int w, int a, int b):
	global filled
	if a > A or b > B:
		return 0
	if w == W:
		return dfs(h+1, 0, a, b)
	if h == H:
		return 1
	if filled[h][w]:
		return dfs(h, w+1, a, b)
	# square
	square = dfs(h, w+1, a, b+1)
	# long tate
	tate = 0
	if h+1 < H:
		filled[h+1][w] = True
		tate = dfs(h, w+1, a+1, b)
		filled[h+1][w] = False
	# long yoko
	yoko = 0
	if w+1 < W:
		yoko = dfs(h, w+2, a+1, b)
	return square + tate + yoko

print(dfs(0, 0, 0, 0))
