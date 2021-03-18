N,M = map(int,input().split())
A = list(map(int,input().split()))
count = [0] * (N + 1)

for i in range(M):
	count[A[i]] += 1

for i in range(M + 1):
	if count[i] == 0:
		mex = i
		break

for i in range(N - M):
	count[A[i]] -= 1
	count[A[i + M]] += 1
	if count[A[i]] == 0:
		mex = min(mex, A[i])

print(mex)
