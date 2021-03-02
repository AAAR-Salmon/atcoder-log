N,K = map(int,input().split())
a = list(map(int,input().split()))
s = sum(a[:K])
ans = s
i = K
while i < N:
	s = s - a[i - K] + a[i]
	ans += s
	i += 1
print(ans)
