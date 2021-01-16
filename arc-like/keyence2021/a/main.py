N = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a_max = [0] * N
a_max[0] = a[0]
for i in range(1,N):
	a_max[i] = max(a_max[i-1], a[i])
c = [0] * N
c[0] = a[0] * b[0]
for i in range(N):
	c[i] = max(c[i-1], a_max[i] * b[i])
print(*c, sep='\n')
