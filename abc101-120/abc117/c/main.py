N,M = map(int,input().split())
X = sorted(map(int,input().split()))
if N >= M:
	print(0)
	exit(0)
distance = [None] * (M-1)
for i in range(M-1):
	distance[i] = X[i+1] - X[i]
distance.sort()
print(sum(distance[:M - N]))
