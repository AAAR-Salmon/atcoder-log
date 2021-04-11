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

for p in permutations('0123456789', n):
	N1 = S1
	N2 = S2
	N3 = S3
	ok = True
	for i in range(n):
		if p[i] == '0' and k[i] in (S1[0], S2[0], S3[0]):
			ok = False
			break
		N1 = N1.replace(k[i], p[i])
		N2 = N2.replace(k[i], p[i])
		N3 = N3.replace(k[i], p[i])
	if ok and int(N1) + int(N2) == int(N3):
		print(N1, N2, N3, sep='\n')
		exit(0)

print('UNSOLVABLE')
