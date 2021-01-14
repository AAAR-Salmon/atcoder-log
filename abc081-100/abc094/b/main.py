N,M,X = map(int,input().split())
sumA = [0] * (N+1)
for a in map(int,input().split()):
	sumA[a] += 1
for i in range(1,N+1):
	sumA[i] += sumA[i-1]
print(min(sumA[N]-sumA[X],sumA[X]))
