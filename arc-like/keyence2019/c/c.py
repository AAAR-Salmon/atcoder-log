from sys import exit
from functools import reduce

def cumsum(A):
	yield 0
	s = 0
	for a in A:
		s += a
		yield s

add = lambda x, y: x+y

N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
if reduce(add,A) < reduce(add,B):
	print(-1)
	exit()

cnt=0
suf=[0]*N
sisuf=0
for i in range(N):
	if A[i] >= B[i]:
		suf[i] = A[i] - B[i]
	else:
		sisuf += B[i] - A[i]
		cnt += 1
suf.sort(reverse=True)
Ssuf=list(cumsum(suf))

ng=-1
ok=N
while ok - ng > 1:
	mid = (ok + ng) // 2
	if Ssuf[mid] >= sisuf:
		ok = mid
	else:
		ng = mid
print(cnt+ok)
