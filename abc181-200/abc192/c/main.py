N,K = input().split()
K = int(K)
a = [None] * (K+1)
a[0] = N
for i in range(K):
	a[i] = ''.join(sorted(a[i]))
	r = ''.join(reversed(a[i]))
	a[i+1] = str(int(r) - int(a[i]))
print(a[K])
