A = input()
B = input()
ans = ''
if len(A) > len(B):
	ans = 'GREATER'
elif len(A) < len(B):
	ans = 'LESS'
else:
	if A > B:
		ans = 'GREATER'
	elif A < B:
		ans = 'LESS'
	else:
		ans = 'EQUAL'
print(ans)
