A,B,C=map(int,input().split())
M=998244353
SA=A*(A+1)//2
SB=B*(B+1)//2
SC=C*(C+1)//2
print(SA*SB*SC%M)
