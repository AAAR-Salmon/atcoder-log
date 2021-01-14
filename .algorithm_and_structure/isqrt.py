def isqrt(num):
	assert(0 <= num)
	left = -1
	right = num+1
	while right - left > 1:
		mid = (left + right) // 2
		if mid ** 2 <= num:
			left = mid
		else:
			right = mid
	return left
