import sys
from collections import deque
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

N,Q = map(int,input().split())
# parent = [None] * N
children = [[] for _ in range(N)]
for _ in range(N-1):
	a,b = map(intm1,input().split())
	children[a].append(b)
	children[b].append(a)

# 親子関係を求める
q = deque([0])
while q:
	n = q.popleft()
	for c in children[n]:
		# parent[c] = n
		children[c].remove(n)
	q.extend(children[n])

# 各部分木のルートに値を足しておく
ans = [0] * N
for _ in range(Q):
	p,x = map(int,input().split())
	ans[p-1] += x

# 親ノードの値を子ノードに足すことを葉まで繰り返す
q = deque([0])
while q:
	n = q.pop()
	for c in children[n]:
		ans[c] += ans[n]
	q.extend(children[n])

print(*ans)
