from collections import defaultdict

N = int(input())
A = defaultdict(lambda: 0)
for a in map(int, input().split()):
	A[a] += 1
B, C = (list(map(int, input().split())) for _ in range(2))

ans = 0
for j in range(N):
	b = B[C[j] - 1]
	ans += A[b]

print(ans)
