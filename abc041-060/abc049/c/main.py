S = ''.join(reversed(input()))
T = ''
words = [''.join(reversed(w)) for w in ['dream', 'erase', 'eraser', 'dreamer']]
i = 0
appendedAny = True
while appendedAny:
	appendedAny = False
	for w in words:
		if i + len(w) <= len(S) and S[i:i+len(w)] == w:
			T += w
			i += len(w)
			appendedAny = True
print('YES' if S == T else 'NO')
