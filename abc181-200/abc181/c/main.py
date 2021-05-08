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

N=int(input())
P=[None]*N
for i in range(N):
	x,y = map(int,input().split())
	P[i] = Point(x, y)

ans = False
for i in range(N - 2):
	for j in range(i + 1, N - 1):
		for k in range(j + 1, N):
			if (P[j] - P[i]).isInline(P[k] - P[i]):
				ans = True
				break
		if ans:
			break
	if ans:
		break
print('Yes' if ans else 'No')
