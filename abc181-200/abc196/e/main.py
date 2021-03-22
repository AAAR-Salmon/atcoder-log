N = int(input())
a = [None] * N
t = [None] * N
for i in range(N):
	a[i], t[i] = map(int,input().split())
Q = int(input())
x = list(map(int,input().split()))

# F(x) = min(A, max(B, x+C))
A = 10 ** 15
B = - 10 ** 15
C = 0

for i in range(N):
	if t[i] == 1:
		A += a[i]
		B += a[i]
		C += a[i]
	elif t[i] == 2:
		A = max(A, a[i])
		B = max(B, a[i])
	else:
		A = min(A, a[i])
		B = min(B, a[i])

for i in range(Q):
	print(min(A, max(B, x[i] + C)))
