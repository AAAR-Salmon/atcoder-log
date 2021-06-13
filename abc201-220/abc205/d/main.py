from itertools import chain


N, Q = map(int, input().split())
A = list(chain([0], map(int, input().split())))
block = [0] * N
for i in range(N):
	block[i] = A[i + 1] - A[i] - 1
blocksum = [0] * N
blocksum[0] = block[0]
for i in range(1, N):
	blocksum[i] = blocksum[i - 1] + block[i]

for _ in range(Q):
	K = int(input())
	l, r = -1, N
	while r - l > 1:
		m = (l + r) // 2
		if blocksum[m] < K:
			l = m
		else:
			r = m
	if l == -1:
		print(K)
	# elif r == N:
	# 	print(K + N)
	else:
		print(A[r] + K - blocksum[l])
