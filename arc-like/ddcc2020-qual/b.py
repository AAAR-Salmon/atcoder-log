N=int(input())
A=list(map(int,input().split()))
S=[0]*N
S[0] = A[0]
for i in range(1,N):
  S[i] = S[i - 1] + A[i]

ok = -1
ng = N
length = S[-1]
while abs(ok - ng) > 1:
  mid = (ok + ng) // 2
  if S[mid] * 2 < length:
    ok = mid
  else:
    ng = mid

if abs(length - S[ok] * 2) < abs(length - S[ok + 1] * 2):
  L = S[ok]
else:
  L = S[ok + 1]
R = length - L
print(abs(L - R))
