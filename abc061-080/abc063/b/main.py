S = input()
appeared = set()
for c in S:
	if c in appeared:
		print('no')
		exit(0)
	else:
		appeared.add(c)
print('yes')
