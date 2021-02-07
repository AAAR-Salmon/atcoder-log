from math import floor, ceil, sqrt

X,Y,R = map(lambda x: round(float(x) * 10000), input().split())

def isqrt_f(n):
	left = -1
	right = n+1
	while right - left > 1:
		mid = (left + right) // 2
		if mid * mid <= n:
			left = mid
		else:
			right = mid
	return left


def isqrt_c(n):
	left = -1
	right = n+1
	while right - left > 1:
		mid = (left + right) // 2
		if mid * mid >= n:
			right = mid
		else:
			left = mid
	return right

ans = 0
for y in range((Y-R+9999) // 10000, (Y+R) // 10000 + 1):
	dx = isqrt_f(R**2-(y*10000-Y)**2)
	ans += (X+dx) // 10000 - (X-dx+9999) // 10000 + 1
print(ans)
