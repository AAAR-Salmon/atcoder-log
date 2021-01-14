N,T = map(int,input().split())
A = sorted(map(int,input().split()))
B = A[:N//2]
B_len = N // 2
C = A[N//2:]
C_len = (N + 1) // 2

sumB = set()
for bit in range(1 << B_len):
	s = 0
	for i in range(B_len):
		if bit & 1 << i:
			s += B[i]
	if s <= T:
		sumB.add(s)
sumB_len = len(sumB)
sumB = sorted(sumB)

sumC = set()
for bit in range(1 << C_len):
	s = 0
	for i in range(C_len):
		if bit & 1 << i:
			s += C[i]
	if s <= T:
		sumC.add(s)

ans = 0
for c in sumC:
	ok = -1
	ng = sumB_len
	while ng - ok > 1:
		mid = (ok + ng) // 2
		if c + sumB[mid] <= T:
			ok = mid
		else:
			ng = mid
	ans = max(ans, c + sumB[ok])

print(ans)
