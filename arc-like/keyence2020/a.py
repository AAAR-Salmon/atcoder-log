H,W,N=map(int,[input() for _ in range(3)])
M=max(H,W)
print((N+M-1)//M)
