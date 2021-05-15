S = input()
o = [str(i) for i in range(10) if S[i] == 'o']
x = [str(i) for i in range(10) if S[i] == 'x']
if len(o) > 4 or len(x) == 10:
	print(0)
	exit(0)

ans = 0
for i in range(10000):
	s = str(i).zfill(4)
	ok = True
	for j in o:
		if j not in s:
			ok = False
			break
	if not ok:
		continue
	for j in x:
		if j in s:
			ok = False
			break
	if ok:
		ans += 1
print(ans)
