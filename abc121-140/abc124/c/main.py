S=input()
cnt1,cnt2=0,0
for i,c in enumerate(S):
  if i % 2 == 0 and c != '0':
    cnt1 += 1
  elif i % 2 == 1 and c != '1':
    cnt1 += 1
for i,c in enumerate(S):
  if i % 2 == 0 and c != '1':
    cnt2 += 1
  elif i % 2 == 1 and c != '0':
    cnt2 += 1
print(min(cnt1,cnt2))
