N = int(''.join(input().split()))
left = 0
right = N
while right - left > 1:
	mid = (left + right) // 2
	if mid ** 2 <= N:
		left = mid
	else:
		right = mid
print('Yes' if left ** 2 == N else 'No')
