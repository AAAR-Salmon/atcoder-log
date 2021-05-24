N = int(input())
ans = 0
for a in map(int,input().split()):
	while a % 2 == 0:
		a //= 2
		ans += 1
print(ans)
