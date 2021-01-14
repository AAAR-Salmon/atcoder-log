N=int(input())
h=list(map(int,input().split()))
cnt=0
while h != [0] * N:
	p0 = True
	for i in range(N):
		if h[i] > 0:
			h[i] -= 1
			if p0 == True:
				cnt += 1
				p0 = False
		else:
			p0 = True
print(cnt)
