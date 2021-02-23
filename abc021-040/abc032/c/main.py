N,K = map(int,input().split())
s = [int(input()) for _ in range(N)]
if 0 in s:
	print(N)
	exit(0)
ans = 0
prod = 1
r = 0
for l in range(N):
	while r < N and prod * s[r] <= K:
		prod *= s[r]
		r += 1
	ans = max(ans, r - l)
	if l == r:
		r += 1
	else:
		prod //= s[l]
print(ans)
