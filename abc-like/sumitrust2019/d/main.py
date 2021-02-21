N = int(input())
S = input()

ans = 0
for k in range(1000):
	t = str(k).zfill(3)
	i = 0
	for c in S:
		if c == t[i]:
			i += 1
			if i == 3:
				ans += 1
				break
print(ans)
