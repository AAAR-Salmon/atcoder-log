N,K,S = map(int,input().split())
A = [S] * K + [S+1 if S < 1000000000 else 1] * (N - K)
print(*A)
