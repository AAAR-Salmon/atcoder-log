N = int(input())
Q = int(input())
transposed = False
R,C = (list(range(N+1)) for _ in range(2))
for _ in range(Q):
	q = list(map(int,input().split()))
	if q[0] == 1 or q[0] == 2:
		if (q[0] == 1) != transposed:
			R[q[1]], R[q[2]] = R[q[2]], R[q[1]]
		else:
			C[q[1]], C[q[2]] = C[q[2]], C[q[1]]
	if q[0] == 3:
		transposed = not transposed
	elif q[0] == 4:
		if not transposed:
			i = R[q[1]]
			j = C[q[2]]
		if transposed:
			i = R[q[2]]
			j = C[q[1]]
		print(N * (i - 1) + j - 1)
