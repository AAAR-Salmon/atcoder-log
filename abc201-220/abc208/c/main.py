N, K = map(int, input().split())
a = list(map(int, input().split()))
A = [(a[i], i) for i in range(N)]
A.sort()

ans = [K // N] * N

for _, i in A[:K % N]:
	ans[i] += 1

print(*ans, sep='\n')
