N = int(input())

ans = 0

for i in range(1,1000000):
	if int(str(i) * 2) <= N:
		ans += 1
	else:
		break

print(ans)
