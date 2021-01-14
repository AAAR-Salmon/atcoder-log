N=int(input())
A=input()
B=input()
C=input()
cnt = -N
for i in range(N):
	cnt += len({A[i], B[i], C[i]})
print(cnt)
