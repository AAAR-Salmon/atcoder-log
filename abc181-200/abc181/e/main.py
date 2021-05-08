N, M = map(int, input().split())
H = sorted(map(int, input().split()))
W = sorted(map(int, input().split()))

# i == 0: (W,H[0])(H[1],H[2])..(H[N-4],H[N-3])(H[N-2],H[N-1])
# i == 1: (H[0],H[1])(W,H[2])..(H[N-4],H[N-3])(H[N-2],H[N-1])
# i == (N-1)//2-1: (H[0],H[1])(H[2],H[3])..(W,H[N-3])(H[N-2],H[N-1])
# i == (N-1)//2: (H[0],H[1])(H[2],H[3])..(H[N-3],H[N-2])(W,H[N-1])
L = [0] * ((N + 1) // 2)
R = [0] * ((N + 1) // 2)

for i in range(1, (N + 1) // 2):
	L[i] = L[i - 1] + H[i * 2 - 1] - H[i * 2 - 2]
for i in range((N - 1) // 2 - 1, -1, -1):
	R[i] = R[i + 1] + H[i * 2 + 2] - H[i * 2 + 1]

ans = 1 << 62

for i in range((N + 1) // 2):
	l, r = 0, M - 1
	while r - l > 1:
		m = (l + r) // 2
		if W[m] >= H[i * 2]:
			r = m
		else:
			l = m
	ans = min(ans, L[i] + R[i] + min(abs(W[r] - H[i * 2]), abs(W[l] - H[i * 2])))

print(ans)
