K = int(input())
x = 0
e = False
for i in range(1, K+1):
	x = (10 * x + 7) % K
	if x == 0:
		e = True
		break
print(i if e else -1)
