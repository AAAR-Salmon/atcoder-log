S = input()
if all(48 <= ord(c) < 58 for c in S):
	print(int(S) * 2)
else:
	print('error')
