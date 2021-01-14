def root(x, n):
	left,right=0,x+1
	while right - left > 1:
		mid = (left + right) // 2
		if mid ** n <= x:
			left = mid
		else:
			right = mid
	return left

N,P=map(int,input().split())
for i in range(root(P, N), 0, -1):
	if P % (i ** N) == 0:
		print(i)
		exit()
