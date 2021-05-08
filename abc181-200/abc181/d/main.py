S=input()
SS={}
for i in range(0,10):
	SS[str(i)] = 0
for c in S:
	SS[c] += 1

ans = False
if S == '8':
	ans = True
elif len(S) == 2:
	for i in range(16,100,8):
		t=str(i)
		tt={}
		for c in t:
			if c not in tt:
				tt[c] = 1
			else:
				tt[c] += 1
		ok = True
		for d in tt.keys():
			if tt[d] > SS[d]:
				ok = False
		if ok:
			ans = True
			break
elif len(S) >= 3:
	for i in range(104,1000,8):
		t=str(i)
		tt={}
		for c in t:
			if c not in tt:
				tt[c] = 1
			else:
				tt[c] += 1
		ok = True
		for d in tt.keys():
			if tt[d] > SS[d]:
				ok = False
		if ok:
			ans = True
			break
print('Yes' if ans else 'No')
