import numpy as np

N = int(input())
pos = [None] * (N+1)
for i in range(1, N+1):
	X,Y = map(int,input().split())
	pos[i] = np.matrix([[X],[Y]])
M = int(input())
A = [None] * (M+1)
b = [None] * (M+1)
A[0] = np.identity(2, dtype=int)
b[0] = np.matrix([[0], [0]])
C = [None] * 4
C[0] = np.matrix([[0, 1], [-1, 0]])
C[1] = np.matrix([[0, -1], [1, 0]])
C[2] = np.matrix([[-1, 0], [0, 1]])
C[3] = np.matrix([[1, 0], [0, -1]])
for i in range(1, M+1):
	op = list(map(int,input().split()))
	if op[0] == 1:
		A[i] = C[0] @ A[i-1]
		b[i] = C[0] @ b[i-1]
	elif op[0] == 2:
		A[i] = C[1] @ A[i-1]
		b[i] = C[1] @ b[i-1]
	elif op[0] == 3:
		d = np.matrix([[op[1]], [0]])
		A[i] = C[2] @ A[i-1]
		b[i] = C[2] @ (b[i-1] - d) + d
	elif op[0] == 4:
		d = np.matrix([[0], [op[1]]])
		A[i] = C[3] @ A[i-1]
		b[i] = C[3] @ (b[i-1] - d) + d

Q = int(input())
for i in range(Q):
	q,p = map(int,input().split())
	x = A[q] @ pos[p] + b[q]
	print(x[0,0], x[1,0])
