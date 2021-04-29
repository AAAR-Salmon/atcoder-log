from math import sqrt

N = int(input())
p = [tuple(map(int,input().split())) for _ in range(N)]
ans = 0
for i in range(N):
	xi, yi = p[i]
	for j in range(i):
		xj, yj = p[j]
		ans = max(ans, sqrt((xj - xi) ** 2 + (yj - yi) ** 2))
print(ans)
