N = int(input())
A = [N] * (N + 1)
A[1] = 1
for i in range(1, N + 1):
	for j in range(i * 2, N + 1, i):
		A[j] = A[i] + 1
print(*A[1:])
