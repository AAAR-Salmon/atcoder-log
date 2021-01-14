N=int(input())
d=0
n=N
while n > 0:
  d += 1
  n //= 10
ans=0
for i in range(1,d+1,2):
  if i == d:
    ans += N + 1 - 10 ** (d - 1)
  else:
    ans += 10 ** i - 10 ** (i - 1)
print(ans)
