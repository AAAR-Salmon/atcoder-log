N = int(input())
S = input()
ans = x = 0
for c in S:
	if c == 'I':
		x += 1
		ans = max(ans, x)
	elif c == 'D':
		x -= 1
print(ans)
