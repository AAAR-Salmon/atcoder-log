N,D,H = map(int,input().split())
obs = [tuple(map(int,input().split())) for _ in range(N)]
d,h = obs[0]
for i in range(N):
	if (H - obs[i][1]) / (D - obs[i][0]) < (H - h) / (D - d):
		d,h = obs[i]
print(max(H - D * (H - h) / (D - d), 0))
