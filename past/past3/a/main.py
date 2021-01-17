s,t = (input() for _ in range(2))
if s == t:
	print('same')
elif s.lower() == t.lower():
	print('case-insensitive')
else:
	print('different')
