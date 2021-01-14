N = int(input())
P = list(map(lambda x:int(x)-1,input().split()))
op = []
i = 0
while i < N - 1:
	if P[i] == i:
		print(-1)
		exit(0)
	p = i
	while P[p] != i:
		if P[p] != p+1 and P[p+1] != i:
			print(-1)
			exit(0)
		p += 1
	for j in range(p,i,-1):
		P[j] = P[j-1]
	P[i] = i
	op += list(range(p,i,-1))
	i = p
print(*op, sep='\n')
