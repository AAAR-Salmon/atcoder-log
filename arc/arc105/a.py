A=list(map(int,input().split()))
y='No'
for i in range(1<<4):
  a=b=0
  for j in range(4):
    if i & 1 << j:
      a += A[j]
    else:
      b += A[j]
  if a == b:
    y='Yes'
print(y)
