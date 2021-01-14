N=int(input())
S=['']*N
P=[0]*N
id=[0]*N
for i in range(N):
  S[i],P[i]=input().split()
  P=list(map(int,P))
  id[i]=i+1

pos = 0
while pos+1 < N:
  if P[pos] < P[pos+1]:
    rp=pos
    while P[rp] < P[rp+1] and rp >= 0:
      S[rp],S[rp+1]=S[rp+1],S[rp]
      P[rp],P[rp+1]=P[rp+1],P[rp]
      id[rp],id[rp+1]=id[rp+1],id[rp]
      rp -= 1
  pos += 1

pos = 0
while pos+1 < N:
  if S[pos] > S[pos+1]:
    rp=pos
    while S[rp] > S[rp+1] and rp >= 0:
      S[rp],S[rp+1]=S[rp+1],S[rp]
      P[rp],P[rp+1]=P[rp+1],P[rp]
      id[rp],id[rp+1]=id[rp+1],id[rp]
      rp -= 1
  pos += 1

for i in id:
  print(i)
