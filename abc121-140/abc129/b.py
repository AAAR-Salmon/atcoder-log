N=int(input())
W=list(map(int,input().split()))
def cumsum(V):
  s=0
  for v in V:
    s += v
    yield s
S=list(cumsum(W))

ok=-1
ng=N
while ng - ok > 1:
  mid = (ok + ng) // 2
  if S[mid] * 2 <= S[-1]:
    ok = mid
  else:
    ng = mid
if S[-1] - S[ok] * 2 < S[ok+1] * 2 - S[-1]:
  S1=S[ok]
  S2=S[-1]-S1
else:
  S1=S[ok+1]
  S2=S[-1]-S1
print(abs(S1 - S2))
