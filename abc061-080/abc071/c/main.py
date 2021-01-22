from sys import set_asyncgen_hooks


N = int(input())
A = map(int,input().split())

B = {}
for a in A:
	if a in B:
		B[a] += 1
	else:
		B[a] = 1

a,b = 0,0
for k in sorted(B.keys(), reverse=True):
	if B[k] >= 4 and a == 0:
		a,b = k,k
	if B[k] >= 2:
		a,b = k,a
	if b != 0:
		break
print(a*b)
