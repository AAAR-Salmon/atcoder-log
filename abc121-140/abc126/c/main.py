import math
N,K=map(int,input().split())
p=0
for i in range(1,N+1):
	p += (1/2) ** max(math.ceil(math.log2(K / i)), 0) / N
print(p)
