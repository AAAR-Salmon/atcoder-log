MOD = 1_000_000_007

N = int(input())
C = sorted(map(int,input().split()))
ans = 1
for i in range(N):
	ans *= max(C[i] - i, 0)
	ans %= MOD
print(ans)
