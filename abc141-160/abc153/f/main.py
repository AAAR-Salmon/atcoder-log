from sys import stderr


N, D, A = map(int, input().split())
R = D * 2
monster = [None] * N
for i in range(N):
	monster[i] = tuple(map(int, input().split()))
monster.sort()
damage = [0] * (N + 1)
cnt = 0
for i in range(N):
	X, H = monster[i]
	damage[i + 1] += damage[i]
	if damage[i + 1] < H:
		addcnt = (H - damage[i + 1] + A - 1) // A
		cnt += addcnt
		damage[i + 1] += addcnt * A
		l, r = i, N
		while r - l > 1:
			m = (l + r) // 2
			if monster[m][0] <= X + R:
				l = m
			else:
				r = m
		if r < N:
			damage[r + 1] -= addcnt * A
print(cnt)
