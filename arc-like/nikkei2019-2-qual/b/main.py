N = int(input())
D = list(map(int,input().split()))
if D[0] != 0:
	print(0)
	exit(0)
dictD = [0] * (max(D) + 1)
for d in D:
	dictD[d] += 1
if dictD[0] > 1:
	print(0)
	exit(0)
ans = 1
for i in range(1, max(D) + 1):
	ans *= dictD[i-1] ** dictD[i]
	ans %= 998244353
print(ans)
