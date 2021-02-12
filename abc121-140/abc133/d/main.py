N = int(input())
A = list(map(int,input().split()))

ans = [0] * N
ans[0] = sum(A[i] * (1 if i % 2 == 0 else -1) for i in range(N))
for i in range(1, N):
	ans[i] = ans[i-1] * -1 + A[i-1] * 2
print(*ans)
