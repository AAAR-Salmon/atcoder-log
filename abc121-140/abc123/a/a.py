d=[0]*5
ok=True
for i in range(5):
  d[i]=int(input())
k=int(input())
for i in range(4):
  for j in range(i+1,5):
    pass
  if abs(d[j] - d[i]) > k:
    ok=False
    break
print('Yay!' if ok else ':(')
