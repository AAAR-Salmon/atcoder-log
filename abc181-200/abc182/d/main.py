def cumsum(A):
	s = 0
	for a in A:
		s += a
		yield s

N=int(input())
A=list(map(int,input().split()))
B=list(cumsum(A))
M=0
Bm=[0]*N
for i in range(N):
	M = max(M, B[i])
	Bm[i] = M
ans=x=0
for i in range(N):
	ans = max(ans, x+Bm[i])
	x = x+B[i]
print(ans)
