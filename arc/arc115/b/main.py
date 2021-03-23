N = int(input())
C = [list(map(int,input().split())) for _ in range(N)]

for i in range(1, N):
	d = C[i][0] - C[0][0]
	for j in range(1, N):
		if C[i][j] - C[0][j] != d:
			print('No')
			exit(0)

print('Yes')

minC = min(min(C[i]) for i in range(N))

minA_index = 0
for i in range(N):
	if C[i][0] < C[minA_index][0]:
		minA_index = i
minB_index = 0
for j in range(N):
	if C[0][j] < C[0][minB_index]:
		minB_index = j
A = [C[i][0] - C[minA_index][0] for i in range(N)]
B = [C[0][j] - C[0][minB_index] + minC for j in range(N)]
print(*A)
print(*B)
