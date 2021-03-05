from itertools import chain
N=int(input())
A=[0]*N
for i in range(N):
  A[i]=int(input())
M=max(A)
doublemax=False
for i in range(N):
  if doublemax:
    print(M)
    continue
  if M == A[i]:
    m = max(chain(A[:i], A[i+1:]))
    if m == M:
      doublemax = True
    print(m)
  else:
    print(M)
