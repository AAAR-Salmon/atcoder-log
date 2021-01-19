N,K = map(int,input().split())
d = [i for i in range(10)]

dp = [False] * 100000

for D in map(int,input().split()):
	d.remove(D)

for i in d:
	dp[i] = True

for i in range(100000):
	for n in d:
		if dp[i] and 10 * i + n < 100000:
			dp[10 * i + n] = True

for i in range(N, 100000):
	if dp[i]:
		print(i)
		break
