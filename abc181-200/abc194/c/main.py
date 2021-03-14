N = int(input())
A = list(map(int,input().split()))
sumA = [0] * (N + 1)
sumSqA = [0] * (N + 1)

for i in range(N):
	sumA[i+1] = sumA[i] + A[i]
	sumSqA[i+1] = sumSqA[i] + (A[i]) ** 2

ans = 0

for i in range(1, N):
	ans += i * A[i] ** 2 + sumSqA[i] - 2 * A[i] * sumA[i]
print(ans)
