N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
X = 0
for j in range(39, -1, -1):
	s = sum(1 for a in A if a >> j & 1)
	if X + (1 << j) <= K and s <= N - s:
		X += 1 << j
		ans += (N - s) * (1 << j)
	else:
		ans += s * (1 << j)

print(ans)
