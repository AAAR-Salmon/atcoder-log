visited = []
A,B,C = map(int,input().split())
visited.append((A,B,C))
ans = 0
while A%2 == B%2 == C%2 == 0:
	a,b,c=A/2,B/2,C/2
	A=b+c
	B=c+a
	C=a+b
	ans += 1
	if (A,B,C) in visited:
		ans = -1
		break
	visited.append((A,B,C))
print(ans)
