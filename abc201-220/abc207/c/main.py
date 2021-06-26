N = int(input())

L = [None] * N
R = [None] * N
for i in range(N):
	t, l, r = map(float, input().split())
	L[i] = l if t == 1 or t == 2 else l + 0.1
	R[i] = r if t == 1 or t == 3 else r - 0.1

ans = 0
for j in range(N):
	for i in range(j):
		if L[i] <= L[j] <= R[i] or L[i] <= R[j] <= R[i] or L[j] <= L[i] <= R[j] or L[j] <= R[i] <= R[j]:
			ans += 1

print(ans)
