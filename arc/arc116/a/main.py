T = int(input())
for _ in range(T):
	N = int(input())
	i = 2
	f = 0
	while N % 2 == 0:
		f += 1
		N //= 2
	if f == 0:
		print('Odd')
	elif f == 1:
		print('Same')
	else:
		print('Even')
