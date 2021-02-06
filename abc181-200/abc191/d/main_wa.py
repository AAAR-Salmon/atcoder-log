from math import floor, ceil, sqrt

X,Y,R = map(float,input().split())
ans = 0
for y in range(ceil(Y-R), floor(Y+R)+1):
	dy = sqrt(R**2-(y-Y)**2)
	ans += floor(X+dy) - ceil(X-dy) + 1
print(ans)
