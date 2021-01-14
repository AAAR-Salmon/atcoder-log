N=int(input())
S=input()
K=int(input())
c=S[K-1]
ans=''
for i,s in enumerate(S):
  ans += s if s == c else '*'
print(ans)
