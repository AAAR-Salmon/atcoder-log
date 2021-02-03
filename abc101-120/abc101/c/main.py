N,K = map(int,input().split())
A = list(map(int,input().split()))
i = A.index(1)
j = i + 1
ans = 0
if i % (K - 1) != 0:
	i = i // (K - 1) * (K - 1)
	j = i + K
	ans += 1
ans += i // (K - 1)
ans += (N - j + K - 2) // (K - 1)
print(ans)
