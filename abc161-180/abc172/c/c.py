def cumsum(A, C):
	yield 0
	s=0
	for a in A:
		s += a
		if s > C:
			return
		yield s

N,M,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
SA=list(cumsum(A,K))
a=len(SA)
SB=list(cumsum(B,K))
b=len(SB)

ans=0
ng=b
for i in range(a):
	ok=-1
	while ng - ok > 1:
		mid = (ok + ng) // 2
		if SA[i] + SB[mid] <= K:
			ok = mid
		else:
			ng = mid
	ans = max(ans, i + ok)
print(ans)
