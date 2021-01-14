import math
class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def isInline(self, P):
		return self.x * P.y - self.y * P.x == 0

	def __sub__(self, P):
		X = self.x - P.x
		Y = self.y - P.y
		return Point(X, Y)

	def distance(self, P):
		X = self.x - P.x
		Y = self.y - P.y
		return math.sqrt(X ** 2 + y ** 2)

N=int(input())
P=[None] * N
R=0
for i in range(N):
	x,y=map(int,input().split())
	P[i]=Point(x,y)
	R=max(R,100-abs(y))

for i in range(N-1):
	for j in range(i+1,N):
		R = max(R, P[i].distance(P[j]))
print(R / 2)
