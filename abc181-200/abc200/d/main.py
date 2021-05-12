from ntpath import sep


N = int(input())
A = list(map(lambda x: int(x) % 200, input().split()))

MOD = 200

dp = [None] * MOD
for b in range(1, 1 << min(N, 8)):
	s = 0
	for i in range(min(N, 8)):
		if b >> i & 1:
			s = (s + A[i]) % MOD
	if dp[s]:
		print('Yes')
		for b2 in (dp[s], b):
			pc = b2
			pc -= pc >> 1 & 0x55
			pc = (pc & 0x33) + (pc >> 2 & 0x33)
			pc = (pc + (pc >> 4)) & 0x0f
			print(pc, end=' ')
			print(*(i + 1 for i in range(min(N, 8)) if b2 >> i & 1), sep=' ')
		exit(0)
	else:
		dp[s] = b
print('No')
