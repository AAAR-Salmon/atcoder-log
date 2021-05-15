from collections import deque

MOD = 1_000_000_007

N = int(input())
edges = [[] for _ in range(N + 1)]
for _ in range(N - 1):
	u, v, w = map(int,input().split())
	edges[u].append((v, w))
	edges[v].append((u, w))

# 先祖のxor求めれば2点間はO(1)で求められる
parent = [0] * (N + 1)
cumxor = [0] * (N + 1)
q = deque([1])
while q:
	p = q.popleft()
	for n, w in edges[p]:
		if parent[n] == 0:
			parent[n] = p
			cumxor[n] = cumxor[p] ^ w
			q.append(n)

ans = 0
for i in range(60):
	O = I = 0
	for a in cumxor[1:]:
		if a & 1 << i:
			I += 1
		else:
			O += 1
	ans = (ans + I * O * (1 << i)) % MOD
print(ans)
