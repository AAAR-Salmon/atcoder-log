N = int(input())
a = [input() for _ in range(N)]
S = ''
for i in range(N // 2):
	issatisfiable = False
	for c in a[i]:
		if c in a[-1-i]:
			S += c
			issatisfiable = True
			break
	if not issatisfiable:
		print(-1)
		exit(0)
print(S, a[N // 2][0] if N % 2 == 1 else '', S[::-1], sep='')
