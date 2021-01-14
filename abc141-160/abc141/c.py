N,K,Q=map(int,input().split())
A=[0]*N
for _ in range(Q):
  a = int(input()) - 1
  A[a] += 1
for a in A:
  print('Yes' if K - Q + a > 0 else 'No')
