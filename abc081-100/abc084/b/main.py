A,B = map(int,input().split())
S = input()
for i in range(A+B+1):
	if i == A:
		if S[i] != '-':
			print('No')
			exit(0)
	elif not ord('0') <= ord(S[i]) <= ord('9'):
		print('No')
		exit(0)
print('Yes')
