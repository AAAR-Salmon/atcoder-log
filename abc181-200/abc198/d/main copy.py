from itertools import chain, permutations

done = [False] * 10
S1 = input()
S2 = input()
S3 = input()

kinds_of_alphabet = set()
for c in chain(S1, S2, S3):
	kinds_of_alphabet.add(c)

k = list(kinds_of_alphabet)
n = len(k)

if n > 10:
	print('UNSOLVABLE')
	exit(0)

x = [0] * n

def dfs(N):
	if N == n:
		N1, N2, N3 = S1, S2, S3
		for i in range(n):
			N1 = N1.replace(k[i], x[i])
			N2 = N2.replace(k[i], x[i])
			N3 = N3.replace(k[i], x[i])
		if int(N1) + int(N2) == int(N3):
			print(N1, N2, N3, sep='\n')
			exit(0)
		return
	for i in range(k[N] in (S1[0], S2[0], S3[0]), 10):
		if done[i]:
			continue
		done[i] = True
		x[N] = str(i)
		dfs(N + 1)
		done[i] = False

dfs(0)
print('UNSOLVABLE')
