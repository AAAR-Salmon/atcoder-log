from collections import defaultdict

N = int(input())
D = [list(map(int, input().split())) for _ in range(N)]
cumsumD = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(N):
	for j in range(N):
		cumsumD[i + 1][j + 1] = cumsumD[i][j + 1] + cumsumD[i + 1][j] - cumsumD[i][j] + D[i][j]
ans = [0] * (N**2 + 1)
for r in range(1, N + 1):
	for c in range(1, N + 1):
		for i in range(N - r + 1):
			for j in range(N - c + 1):
				ans[r * c] = max(ans[r * c], cumsumD[i + r][j + c] - cumsumD[i][j + c] - cumsumD[i + r][j] + cumsumD[i][j])

for i in range(N**2):
	ans[i + 1] = max(ans[i], ans[i + 1])

Q = int(input())
for _ in range(Q):
	P = int(input())
	print(ans[P])
