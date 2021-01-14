S=input()
a,b=int(S[:2]),int(S[2:])
if (a > 12 or a == 0) and (b > 12 or b == 0):
	print('NA')
elif a > 12 or a == 0:
	print('YYMM')
elif b > 12 or b == 0:
	print('MMYY')
else:
	print('AMBIGUOUS')
