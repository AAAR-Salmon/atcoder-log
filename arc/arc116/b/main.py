MOD = 998244353

N = int(input())
A = list(map(int,input().split()))
A.sort()

ans = 0
for i in range(N):
	ans = (ans + A[i] * A[i]) % MOD
	pow2 = 1
	for j in range(i + 1, N):
		ans = (ans + A[i] * A[j] * pow2) % MOD
		pow2 = (pow2 * 2) % MOD
print(ans)
