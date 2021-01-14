N=int(input())
ans=0
for _ in range(N):
	s=list(input().split())
	if s[1] == 'JPY':
		ans += float(s[0])
	else:
		ans += float(s[0]) * 380000.0
print(ans)
