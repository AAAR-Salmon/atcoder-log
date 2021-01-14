N,L=map(int,input().split())
sum=(2*L+N-1)*N//2
if sum > 0:
  if L < 0:
    print(sum)
  else:
    print(sum - L)
else:
  if L + N - 1 > 0:
    print(sum)
  else:
    print(sum - (L + N - 1))
