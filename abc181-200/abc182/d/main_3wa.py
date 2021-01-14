def cumsum(A):
	s = 0
	for a in A:
		s += a
		yield s

N=int(input())
A=list(map(int,input().split()))
B=list(cumsum(A))
C=list(cumsum(B))
M,I=0,-1
for i in range(N):
	if C[i] >= M:
		M = C[i]
		I = i
if I == -1:
	print(0)
else:
	ans=M
	if I+1 == N:
		ans = max(ans,M-C[I]+max(B[:I]))
	else:
		ans = max(ans, M+max(B[:I+1]), M-C[I]+max(B[:I]))
	print(ans)
