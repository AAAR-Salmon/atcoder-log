from collections import deque

H,W = map(int,input().split())
A = [input() for _ in range(H)]
dp = [[None] * W for _ in range(H)]
dp[-1][-1] = 0

def sgn(c):
	return (c == '+') * 2 - 1

q = deque([(H - 2, W - 1), (H - 1, W - 2)])
while q:
	x,y = q.popleft()
	if x < 0 or y < 0:
		continue
	if dp[x][y] != None:
		continue
	if x + 1 < H and y + 1 < W:
		# (x, y) -> (x + 1, y) or (x, y + 1)
		if (x + y) % 2 == 0: # Takahashi
			dp[x][y] = max(dp[x + 1][y] + sgn(A[x + 1][y]),
			               dp[x][y + 1] + sgn(A[x][y + 1]))
		else: # Aoki
			dp[x][y] = min(dp[x + 1][y] - sgn(A[x + 1][y]),
			               dp[x][y + 1] - sgn(A[x][y + 1]))
	elif x + 1 < H:
		# (x, y) -> (x + 1, y)
		if (x + y) % 2 == 0: # Takahashi
			dp[x][y] = dp[x + 1][y] + sgn(A[x + 1][y])
		else: # Aoki
			dp[x][y] = dp[x + 1][y] - sgn(A[x + 1][y])
	else:
		# (x, y) -> (x, y + 1)
		if (x + y) % 2 == 0:  # Takahashi
			dp[x][y] = dp[x][y + 1] + sgn(A[x][y + 1])
		else: # Aoki
			dp[x][y] = dp[x][y + 1] - sgn(A[x][y + 1])
	q.append((x - 1, y))
	q.append((x, y - 1))

if dp[0][0] > 0:
	print('Takahashi')
elif dp[0][0] < 0:
	print('Aoki')
else:
	print('Draw')
