N=int(input())
A,B=map(int,input().split())
P=list(map(int,input().split()))
a=b=c=0
for p in P:
	if p <= A:
		a += 1
	elif p <= B:
		b += 1
	else:
		c += 1
print(min(a,b,c))
