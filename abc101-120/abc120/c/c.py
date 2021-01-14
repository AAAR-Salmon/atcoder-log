S=input()
r=b=0
for c in S:
	if c == '0':
		r += 1
	else:
		b += 1
print(min(r,b)*2)
