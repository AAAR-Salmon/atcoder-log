class Pair:
	def __init__(self, first, second):
		self.first = first
		self.second = second

ans=cnt=0
N,M=map(int,input().split())
A=[0]*N
for i in range(N):
	a,b=map(int,input().split())
	A[i] = Pair(a, b)

A.sort(key=lambda A:A.first)

for i in range(N):
	if cnt + A[i].second > M:
		ans += (M - cnt) * A[i].first
		cnt = M
		break
	else:
		ans += A[i].first * A[i].second
		cnt += A[i].second
print(ans)
