N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
ans=0
rem=A[0]
for i in range(N):
  if rem + A[i+1] < B[i]:
    ans += rem + A[i+1]
    rem = 0
  else:
    ans += B[i]
    if rem < B[i]:
      rem = rem + A[i+1] - B[i]
    else:
      rem = A[i+1]
print(ans)
