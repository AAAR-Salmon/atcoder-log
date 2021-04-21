N = int(input())
S = input()

lb = 0
rw = S.count('.')

ans = rw

for c in S:
	if c == '#':
		lb += 1
	else:
		rw -= 1
	ans = min(ans, lb + rw)

print(ans)
