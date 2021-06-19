N = int(input())

cur = 0
for d in range(1000000):
	cur += d
	if cur >= N:
		print(d)
		break
