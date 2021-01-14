S=input()
ans=cnt=0
for c in S:
  if c in 'ACGT':
    cnt += 1
    if cnt > ans:
      ans = cnt
  else:
    cnt = 0
print(ans)
