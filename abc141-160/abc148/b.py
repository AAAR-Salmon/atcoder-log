N=int(input())
S,T=input().split(' ')
U=''
for i in range(N):
  U += S[i] + T[i]
print(U)
