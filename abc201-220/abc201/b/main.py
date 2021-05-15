N = int(input())
M = [None] * N
for i in range(N):
	S, T = input().split()
	T = int(T)
	M[i] = (T, S)
M.sort()
print(M[-2][1])
