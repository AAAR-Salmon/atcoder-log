N,K = map(int,input().split())
ans = 0
F = sorted(tuple(map(int,input().split())) for _ in range(N))
for a,b in F:
	if a <= ans + K:
		K = K - (a - ans) + b
		ans = a
	else:
		ans += K
		K = 0
		break
print(ans + K)
