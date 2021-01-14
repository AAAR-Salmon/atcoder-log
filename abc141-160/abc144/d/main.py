import math
from math import sin
from math import cos
from math import tan
from functools import reduce
from collections import deque

def v(a,b,t):
	if b*cos(t) <= a*sin(t):
		return a*b*b/2/tan(t)
	else:
		return a*a*(2*b-a*tan(t))/2

a,b,x = map(float,input().split())
left = 0
right = 90
while right - left > 10**(-7):
	mid = (left+right) / 2
	if v(a,b,math.radians(mid)) > x:
		left = mid
	else:
		right = mid
print(left)
