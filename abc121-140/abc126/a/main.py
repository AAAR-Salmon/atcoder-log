N,K=map(int,input().split())
K-=1
S=input()
S=S[:K] + S[K].lower() + S[K+1:]
print(S)
