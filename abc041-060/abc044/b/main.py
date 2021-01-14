w = input()
d = {}
for c in w:
	if c in d:
		d[c] += 1
	else:
		d[c] = 1
print('Yes' if all(map(lambda t: t%2==0, d.values())) else 'No')
