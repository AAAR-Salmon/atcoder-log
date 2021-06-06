N = int(input())
T = list(map(int, input().split()))
sumT = sum(T)
dp = {0}

for t in T:
	dp_ = dp.copy()
	for x in dp_:
		if x + t <= sumT // 2:
			dp.add(x + t)

print(sumT - max(dp))
