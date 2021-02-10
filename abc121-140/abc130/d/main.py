N,K = map(int,input().split())
a = list(map(int,input().split()))
sa = [0] * (N+1)
for i in range(N):
	sa[i+1] = sa[i] + a[i]

i = 0
ans = 0
while sa[N] - sa[i] >= K:
	j = N+1
	jm1 = 0
	while j - jm1 > 1:
		mid = (j + jm1) // 2
		if sa[mid] - sa[i] >= K:
			j = mid
		else:
			jm1 = mid
	ans += N - j + 1
	i += 1
print(ans)
