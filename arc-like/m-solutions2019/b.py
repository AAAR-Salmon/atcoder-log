S=input()
cnt=0
for c in S:
  if c == 'o': cnt += 1
print('YES' if cnt + 15 - len(S) >= 8 else 'NO')
