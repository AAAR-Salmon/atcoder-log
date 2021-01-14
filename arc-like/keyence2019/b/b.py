S = input()
N = len(S)
s = 'keyence'
ok = False
if s in S:
	ok = True
for i in range(1,7):
	if s[:i] == S[:i] and s[i:] == S[-(7-i):]:
		ok = True
print('YES' if ok else 'NO')
