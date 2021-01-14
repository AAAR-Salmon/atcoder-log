S=input()
pS=S[0]
cnt=1
pos=1
while pos < len(S):
  if pS == S[pos]:
    if pos+1 < len(S):
      pS = S[pos:pos+2]
      pos += 2
      cnt += 1
    else:
      pos += 1
  else:
    pS = S[pos]
    pos += 1
    cnt += 1
print(cnt)
