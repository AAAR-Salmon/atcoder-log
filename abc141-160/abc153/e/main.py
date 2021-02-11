H,N = map(int,input().split())
A = [None] * N
B = [None] * N
for i in range(N):
	A[i],B[i] = map(int,input().split())

dp = [10**9] * 20001
dp[0] = 0
for i in range(H):
	for j in range(N):
		dp[i+A[j]] = min(dp[i+A[j]], dp[i] + B[j])
print(min(dp[H:]))

