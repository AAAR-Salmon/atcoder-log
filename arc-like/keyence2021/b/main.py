from collections import deque

N,K = map(int,input().split())
a = sorted(map(int,input().split()))
q = deque(a)

ans = 0
fin = False
for num in range(N+1):
	for i in range(K):
		if not q:
			fin = True
			break
		n = q.popleft()
		if n > num:
			q.appendleft(n)
			K = i
			break
		else:
			ans += 1
	if fin:
		break
	while q:
		n = q.popleft()
		if n != num:
			q.appendleft(n)
			break
print(ans)
