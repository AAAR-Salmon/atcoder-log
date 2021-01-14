def popcount(bits):
	ret = 0
	while bits:
		ret += bits & 1
		bits >>= 1
	return ret

N = int(input())
H = [[None] * N for _ in range(N)] * N
for i in range(N):
	A = int(input())
	for j in range(A):
		x,y = map(int,input().split())
		H[i][x - 1] = y == 1

ans = 0
for bits in range(1 << N):
	ok = True
	for i in range(N):
		if 1 << i & bits:
			for j in range(N):
				if H[i][j] is not None:
					if not H[i][j] and 1 << j & bits or H[i][j] and not 1 << j & bits:
						ok = False
						break
		if not ok:
			break
	if ok:
		ans = max(ans, popcount(bits))
print(ans)
