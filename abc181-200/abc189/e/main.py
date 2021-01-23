N = int(input())
pos = [None] * (N+1)
for i in range(1, N+1):
	pos[i] = tuple(map(int,input().split()))

M = int(input())
A = [None] * (M+1)
b = [None] * (M+1)
A[0] = [1,0,
        0,1]
b[0] = [0,0]

for i in range(1, M+1):
	op = input().split()
	A_ = A[i-1]
	b_ = b[i-1]
	if op[0] == '1':
		A[i] = [A_[2], A_[3],
		        -A_[0], -A_[1]]
		b[i] = [b_[1], -b_[0]]
	elif op[0] == '2':
		A[i] = [-A_[2], -A_[3],
		        A_[0], A_[1]]
		b[i] = [-b_[1], b_[0]]
	elif op[0] == '3':
		p = int(op[1])
		A[i] = [-A_[0], -A_[1],
		        A_[2], A_[3]]
		b[i] = [-b_[0] + 2 * p, b_[1]]
	# elif op[0] == '4':
	else:
		p = int(op[1])
		A[i] = [A_[0], A_[1],
		        -A_[2], -A_[3]]
		b[i] = [b_[0], -b_[1] + 2 * p]

Q = int(input())
for i in range(Q):
	q,p = map(int,input().split())
	x,y = pos[p]
	A_ = A[q]
	b_ = b[q]
	print(A_[0] * x + A_[1] * y + b_[0],
	      A_[2] * x + A_[3] * y + b_[1])
