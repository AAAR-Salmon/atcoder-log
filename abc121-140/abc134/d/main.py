N = int(input())
a = list(map(int,input().split()))
b = [0] * (N + 1)
for i in range(N, 0, -1):
	if i * 2 > N:
		b[i] = a[i - 1]
	else:
		b[i] = sum(b[i * 2::i]) & 1 ^ a[i - 1]
M = sum(b)
print(M)
if M > 0:
	print(*(i for i in range(N + 1) if b[i]))
