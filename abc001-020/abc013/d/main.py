N, M, D = map(int,input().split())
pm = list(range(N))
for i in reversed(list(map(int,input().split()))):
	pm[i - 1], pm[i] = pm[i], pm[i - 1]

ans = list(range(N))

while D > 0:
	if D & 1:
		for i in range(N):
			ans[i] = pm[ans[i]]
	pm_ = pm[:]
	for i in range(N):
		pm[i] = pm_[pm[i]]
	D >>= 1

print(*map(lambda x: x + 1, ans), sep='\n')
