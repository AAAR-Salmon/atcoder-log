N = int(input())

def mbin(n):
	if n == 0:
		return '0'
	elif n % 2 == 0:
		return mbin(n // -2) + '0'
	else:
		return mbin(n - 1)[:-1] + '1'

print(mbin(N))
