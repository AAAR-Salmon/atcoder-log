MOD = 1_000_000_007
N,P = map(int,input().split())
print((P-1)*pow(P-2,N-1,MOD)%MOD)
