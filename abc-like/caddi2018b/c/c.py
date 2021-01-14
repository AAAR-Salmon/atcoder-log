N,P=map(int,input().split())
if N == 1:
	print(P)
	exit()
PF={}
i=2
while P > 1:
	for i in range(i,1000001):
		if P % i == 0:
			if i in PF:
				PF[i] += 1
			else:
				PF[i] = 1
			P //= i
			break
ans=1
for p,k in PF.items():
	ans *= p ** (k//N)
print(ans)
