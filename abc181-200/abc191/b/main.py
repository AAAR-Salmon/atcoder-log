N,X = map(int,input().split())
ans = []
for a in map(int, input().split()):
	if a != X:
		ans.append(a)
print(*ans)
