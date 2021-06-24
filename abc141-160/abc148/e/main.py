N=int(input())
cnt = 0
if N % 2 == 0:
  q = 10
  while q <= N:
    cnt += N // q
    q *= 5
print(cnt)
