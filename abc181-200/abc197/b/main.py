H,W,X,Y = map(int,input().split())
S = [input() for _ in range(H)]
X -= 1
Y -= 1
ans = 0
for x in range(X, H):
	if S[x][Y] == '.':
		ans += 1
	else:
		break
for x in range(X-1, -1, -1):
	if S[x][Y] == '.':
		ans += 1
	else:
		break
for y in range(Y+1, W):
	if S[X][y] == '.':
		ans += 1
	else:
		break
for y in range(Y-1, -1, -1):
	if S[X][y] == '.':
		ans += 1
	else:
		break
print(ans)
