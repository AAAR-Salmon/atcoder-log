S = input()
T = input()
f = [None] * 26
for i in range(len(S)):
	s = ord(S[i]) - 97
	if f[s] == None:
		f[s] = T[i]
	else:
		if f[s] != T[i]:
			print('No')
			exit(0)
for i in range(26):
	for j in range(i):
		if f[i] == f[j] and f[i] != None:
			print('No')
			exit(0)
print('Yes')
