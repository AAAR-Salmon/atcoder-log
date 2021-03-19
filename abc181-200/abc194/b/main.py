N = int(input())
A = [None] * N
B = [None] * N
for i in range(N):
	A[i], B[i] = map(int,input().split())

ans = 100000
for i in range(N):
	for j in range(N):
		if i == j:
			ans = min(ans, A[i] + B[j])
		else:
			ans = min(ans, max(A[i], B[j]))

print(ans)
