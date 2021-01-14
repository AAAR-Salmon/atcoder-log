import math
A,B,K=map(int,input().split())
ans=g=math.gcd(A,B)
for i in range(K):
	while g % ans != 0:
		ans -= 1
	if i + 1 != K:
		ans -= 1
print(ans)
