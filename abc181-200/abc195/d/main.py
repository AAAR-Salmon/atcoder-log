N,M,Q = map(int,input().split())
baggage = [None] * N
for i in range(N):
	W,V = map(int,input().split())
	baggage[i] = (W,V)
X = list(map(int,input().split()))

baggage.sort(reverse=True, key=lambda x:x[1])
for i in range(Q):
	L,R = map(int,input().split())
	box = X[:L-1] + X[R:]
	box.sort()
	ans = 0
	picked = 0
	j = 0
	box_n = M - (R - L + 1)
	while j < N and picked < box_n:
		W,V = baggage[j]
		if W > box[-1]:
			j += 1
			continue
		ans += V
		l = -1
		r = box_n - picked
		while r - l > 1:
			m = (l + r) // 2
			if box[m] >= W:
				r = m
			else:
				l = m
		box.pop(r)
		j += 1
		picked += 1
	print(ans)

