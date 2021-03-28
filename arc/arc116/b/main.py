MOD = 998244353

N = int(input())
A = list(map(int,input().split()))
A.sort()

ans = 0

S = 0
for i in range(N - 1, -1, -1):
	ans = (ans + A[i] * (A[i] + S)) % MOD
	S = (2 * S + A[i]) % MOD
print(ans)
