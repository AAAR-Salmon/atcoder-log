from sys import exit
def f(n):
	if n % 2 == 0:
		return n // 2
	else:
		return 3 * n + 1

dp=[int(input())]
i=0
while True:
	a = f(dp[i])
	i += 1
	if a in dp:
		print(i+1)
		exit()
	else:
		dp.append(a)
