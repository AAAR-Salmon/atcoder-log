N = int(input())
balls = [None] * N
for j in range(N):
	X,C = map(int,input().split())
	balls[j] = (C,X)
balls.sort()
dp = [None] * (N + 1)
x = [None] * (N + 1)
dp[0] = (0, 0)
x[0] = (0, 0)
i = 0
l = r = 0
while l < N:
	c = balls[l][0]
	for j in range(l, N):
		if balls[j][0] != c:
			break
		r = j
	x[i + 1] = (xl, xr) = balls[l][1], balls[r][1]
	pxl, pxr = x[i]
	dl, dr = dp[i]
	dp[i + 1] = (min(dl + abs(xr - pxl), dr + abs(xr - pxr)) + xr - xl, min(dl + abs(xl - pxl), dr + abs(xl - pxr)) + xr - xl)
	i += 1
	l = r + 1
print(min(dp[i][0] + abs(x[i][0]), dp[i][1] + abs(x[i][1])))
